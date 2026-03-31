import requests
from logging import getLogger
from dataclasses import dataclass
from decimal import decimal


@dataclass
class CurrencyApiClient:
    http_client: requests.Session
    logger: getLogger()

    def get_exchange_rate(self, currency_code: str) -> decimal:
        try:
            response = self.http_client.get(
                f"https://api.currencyapi.com/v3/latest?apikey=YOUR_API_KEY&base_currency=USD&currencies={currency_code}"
            )
            if not response.ok:
                self.logger.error(
                    f"Error fetching exchange rate for {currency_code}: {response.status_code}"
                )
                return None
            
            if response.json()["data"][currency_code] is None:
                self.logger.error(f"Exchange rate for {currency_code} not found")
                return None
            
            return decimal(response.json()["data"][currency_code])
        except Exception as e:
            self.logger.error(f"Error fetching exchange rate for {currency_code}: {e}")
            return None
