import { CurrencyApiResponse } from "../typescript-before/currency-api-response";



export class CurrencyApiClient {
  async getExchangeRate(currencyCode: string): Promise<number> {
    try {
      const response = await fetch(
        `https://api.currencyapi.com/v3/latest?apikey=YOUR_API_KEY&base_currency=USD&currencies=${currencyCode}`,
      );
      if (!response.ok) {
        throw new Error(`Failed to fetch exchange rate for ${currencyCode}: ${response.statusText}`);
      }
      const data = (await response.json()) as CurrencyApiResponse;
      if (!data.data[currencyCode]) {
        throw new Error(`Exchange rate for ${currencyCode} not found: ${JSON.stringify(data)}`);
      }
      return Number(data.data[currencyCode]);
    } catch (error) {
      throw new Error(`Error fetching exchange rate for ${currencyCode}: ${error.message}`);
    }
  }
}
