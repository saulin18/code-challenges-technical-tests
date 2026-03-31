
from dataclasses import dataclass, field
from decimal import decimal

@dataclass
class CurrencyApiResponse:
    data: dict[str, decimal] = field(default_factory=dict)