import { CurrencyApiClient } from "./currency-api-client";
import { ExchangeRateResponse } from "./exchange-rate-response";


class CurrencyConversion {
  async handle(currencyCode: string, amount: number, currencyClient: CurrencyApiClient): Promise<ExchangeRateResponse> {
    if (!currencyCode || currencyCode.length !== 3 || !currencyCode.toUpperCase().match(/^[A-Z]{3}$/)) {
      throw new Error("Currency code must be a 3-letter uppercase code (e.g., EUR, GBP)");
    }
    if (amount <= 0) {
      throw new Error("Amount must be a positive number");
    }

    const rate = await currencyClient.getExchangeRate(currencyCode);
    if (!rate) {
      throw new Error(`Exchange rate for ${currencyCode} not found or API error occurred`);
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
}