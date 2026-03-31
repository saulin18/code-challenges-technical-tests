import { Semaphore } from "../../../../../semaphore-mutex";
import { CurrencyApiClient } from "./currency-api-client";
import { ExchangeRateResponse } from "./exchange-rate-response";

export class CacheEntry {
  rate: number;
  createdAt: Date;
}

export class CurrencyConversion {
  private readonly cache: Map<string, CacheEntry> = new Map();
  private readonly cacheDuration: number = 5 * 60 * 1000;
  private readonly locks: Map<string, Semaphore> = new Map();
  async handle(
    currencyCode: string,
    amount: number,
    currencyClient: CurrencyApiClient,
  ): Promise<ExchangeRateResponse> {
    if (
      !currencyCode ||
      currencyCode.length !== 3 ||
      !currencyCode.toUpperCase().match(/^[A-Z]{3}$/)
    ) {
      throw new Error(
        "Currency code must be a 3-letter uppercase code (e.g., EUR, GBP)",
      );
    }
    if (amount < 0) {
      throw new Error("Amount must be a positive number");
    }

    const rate = await this.getExchangeRate(currencyCode, currencyClient);
    if (rate === undefined || rate === null) {
      throw new Error(
        `Exchange rate for ${currencyCode} not found or API error occurred`,
      );
    }

    const convertedAmount = amount * rate;
    return {
      currency: currencyCode,
      baseCurrency: "USD",
      rate: rate,
      amount: amount,
      convertedAmount: convertedAmount,
    };
  }

  private isFresh(entry: CacheEntry): boolean {
    return Date.now() - entry.createdAt.getTime() < this.cacheDuration;
  }

  private async getExchangeRate(
    currencyCode: string,
    currencyClient: CurrencyApiClient,
  ): Promise<number> {
    const entry = this.cache.get(currencyCode);
    if (entry && this.isFresh(entry)) {
      return entry.rate;
    }

    const semaphore = this.locks.get(currencyCode) || new Semaphore(1);
    this.locks.set(currencyCode, semaphore);

    const acquired = await Promise.race([
      semaphore.acquire(),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error("Timeout")), 5000),
      ),
    ]);

    if (!acquired) {
      throw new Error("Timeout");
    }

    try {
      const entry = this.cache.get(currencyCode);
      if (entry && this.isFresh(entry)) {
        return entry.rate;
      }

      const rate = await currencyClient.getExchangeRate(currencyCode);

      if (rate) {
        this.cache.set(currencyCode, { rate: rate, createdAt: new Date() });
        return rate;
      }

      if (!rate) throw new Error("Rate doesnt exist");

      return rate;
    } catch (error) {
      throw new Error(
        `Error fetching exchange rate for ${currencyCode}: ${error.message}`,
      );
    } finally {
      semaphore.release();
    }
  }
}
