import asyncio
import random
import time



class CircuitBreaker:
    """
    Circuit Breaker pattern implementation
    """

    def __init__(
        self, failure_threshold: int = 5, timeout: int = 60, success_threshold: int = 3
    ):
        """
        Initialize the Circuit Breaker
        Args:
            failure_threshold: The number of failures before the circuit breaker trips
            timeout: The time in seconds before the circuit breaker resets
            success_threshold: The number of successes before the circuit breaker resets
            failure_count: The number of failures
            success_count: The number of successes
            last_failure_time: The time of the last failure
            is_open: Whether the circuit breaker is open
        """

        self.failure_threshold: int = failure_threshold
        self.timeout: int = timeout
        self.success_threshold: int = success_threshold
        self.failure_count: int = 0
        self.success_count: int = 0
        self.last_failure_time: float = None
        self.is_open: bool = False

    async def call(self, func, *args, **kwargs):
        # El circuit breaker no puede estar abierto
        if self.is_open:
            if not self._should_attempt_reset():
                raise Exception("Circuit breaker is open")
            try:
                result = await func(*args, **kwargs)
                self._record_success()
                return result
            except Exception as e:
                self._record_failure()
                raise e from e
  
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            self._record_failure()
            raise e from e

    def _should_attempt_reset(self):
        """
        Determine if the circuit breaker should attempt to reset
        Returns:
            bool: True if the circuit breaker should attempt to reset, False otherwise
        """
        return (
            self.is_open
            and self.last_failure_time is not None 
            and time() - self.last_failure_time > self.timeout
        )
   
    def _record_success(self):
        self.success_count += 1
        if self.success_count >= self.success_threshold:
            self.is_open = False
            self.success_count = 0
            self.last_failure_time = None
        
    def _record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.is_open = True    
    
    
# Test del circuit breaker
async def unreliable_service():
    if random.random() < 0.7:  # 70% de fallos
        raise Exception("Service unavailable")
    return "Success"


# Probar con diferentes escenarios
if __name__ == "__main__":
    failure_threshold = 5
    timeout = 60
    success_threshold = 3

    async def main():
        circuit_breaker = CircuitBreaker(
            failure_threshold=failure_threshold,
            timeout=timeout,
            success_threshold=success_threshold,
        )

        for i in range(10):
            try:
                result = await circuit_breaker.call(unreliable_service)
                print(f"Result {i}: {result}")
            except Exception as e:
                print(f"Error {i}: {e}")

    asyncio.run(main())
