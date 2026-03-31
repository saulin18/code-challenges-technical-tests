from dataclasses import dataclass
from decimal import decimal
@dataclass
class ExchangeRateResponse:
    currency: str
    base_currency: str
    rate: decimal
    amount: decimal
    converted_amount: decimal