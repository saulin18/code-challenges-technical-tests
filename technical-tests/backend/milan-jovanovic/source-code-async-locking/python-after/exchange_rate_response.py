from dataclasses import dataclass
from decimal import Decimal
@dataclass
class ExchangeRateResponse:
    currency: str
    base_currency: str
    rate: Decimal
    amount: Decimal
    converted_amount: Decimal