from decimal import decimal
from currency_api_client import CurrencyApiClient
from exchange_rate_response import ExchangeRateResponse


class CurrencyConversion:

    @staticmethod
    async def handle(
        currency_code: str, amount: decimal, currency_client: CurrencyApiClient
    ) -> ExchangeRateResponse:
        if not currency_code or len(currency_code) != 3 or not currency_code.isupper():
            raise ValueError(
                "Currency code must be a 3-letter uppercase code (e.g., EUR, GBP)"
            )
        if amount < 0:
            raise ValueError("Amount must be a positive number")
        rate = await currency_client.get_exchange_rate(currency_code)
        if rate is None:
            raise ValueError(f"Exchange rate for {currency_code} not found")
        
        converted_amount = amount * rate
        return ExchangeRateResponse(
            currency=currency_code,
            base_currency="USD",
            rate=rate,
            amount=amount,
            converted_amount=converted_amount,
        )
