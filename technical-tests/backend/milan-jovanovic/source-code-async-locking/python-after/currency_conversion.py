import asyncio
from dataclasses import dataclass, field
from decimal import Decimal
from currency_api_client import CurrencyApiClient
from exchange_rate_response import ExchangeRateResponse
from asyncio import Semaphore
from datetime import datetime, timezone, timedelta


@dataclass
class CacheEntry:
    rate: Decimal = field(default_factory=Decimal)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class CurrencyConversion:

    _locks: dict[str, Semaphore] = {}
    _cache: dict[str, CacheEntry] = {}
    _cache_duration: timedelta = timedelta(minutes=5)

    
    async def handle(
        self, currency_code: str, amount: Decimal, currency_client: CurrencyApiClient
    ) -> ExchangeRateResponse:
        if not currency_code or len(currency_code) != 3 or not currency_code.isupper():
            raise ValueError(
                "Currency code must be a 3-letter uppercase code (e.g., EUR, GBP)"
            )
        if amount < 0:
            raise ValueError("Amount must be a positive number")

        rate = await self.get_exchange_rate(currency_code, currency_client)
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

    async def get_exchange_rate(
        self, currency_code: str, currency_client: CurrencyApiClient
    ) -> Decimal:

        if self._cache.get(currency_code) and self.is_fresh(self._cache[currency_code]):
            return self._cache[currency_code].rate

        # This gets the lock from the dictionary or we create a new one if it doesn't exist
        semaphore = self._locks.get(currency_code, Semaphore(1))
        self._locks[currency_code] = semaphore

        try:
            await asyncio.wait_for(semaphore.acquire(), timeout=5)
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError(
                f"Could not acquire lock for currency code: {currency_code}"
            )

        try:
            if self._cache.get(currency_code) and self.is_fresh(
                self._cache[currency_code]
            ):
                return self._cache[currency_code].rate

            rate = await currency_client.get_exchange_rate(currency_code)
            if rate is None:
                raise ValueError(f"Exchange rate for {currency_code} not found")

            self._cache[currency_code] = CacheEntry(
                rate=rate, created_at=datetime.now(timezone.utc)
            )
            return rate
        finally:
            semaphore.release()

    def is_fresh(self, entry: CacheEntry) -> bool:
        return datetime.now(timezone.utc) - entry.created_at < self._cache_duration
