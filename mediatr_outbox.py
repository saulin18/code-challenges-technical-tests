# Ejercicio 1: Implementar Circuit Breaker
# Tarea: Completar la implementación del Circuit Breaker
from time import time
from abc import ABC
from typing import List
from logging import getLogger


logger = getLogger(__name__)


class Event(ABC):
    def __init__(self, event_type: str, data: dict, version: int = 0):
        self.type = event_type
        self.data = data
        self.timestamp = time()
        self.version: int = version


class AccountCreatedEvent(Event):
    def __init__(self, account_id: str):
        super().__init__(
            "AccountCreated",
            {"account_id": account_id},
        )


class MoneyDepositedEvent(Event):
    def __init__(self, account_id: str, amount: float, account_amount: float = None):
        super().__init__(
            "MoneyDeposited",
            {
                "account_id": account_id,
                "amount": amount,
                "account_amount": account_amount,
            },
        )


class MoneyWithdrawnEvent(Event):
    def __init__(self, account_id: str, amount: float, account_amount: float):
        super().__init__(
            "MoneyWithdrawn",
            {
                "account_id": account_id,
                "amount": amount,
                "account_amount": account_amount,
            },
        )


class Mediatr:
    """Mediator pattern implementation
    This class is used to publish events to the appropriate handlers
    
    I only made this for fun, was not necessary to implement a mediator in this case.
    """
    instance = None
    handlers: dict[type[Event], list["EventHandler"]] = {}

    def __new__(cls):
        new_instance = super(Mediatr, cls).__new__(cls)
        if cls.instance is not None:
            logger.debug("Mediatr instance already exists")
            return cls.instance
        cls.instance = new_instance

        logger.debug("Creating new Mediatr instance")
        return new_instance

    @classmethod
    def get_instance(cls):
        """Get the instance of the Mediatr class
        If the instance is not created, create it and return it
        """
        if cls.instance is None:
            logger.debug("Creating new Mediatr instance")
            cls.instance = Mediatr()
        else:
            logger.debug("Mediatr instance already exists")
        return cls.instance
    
    def publish(self, event: Event) -> None:
        handlers = self.handlers.get(type(event), [])
        for handler in handlers:
            handler.handle(event)



class EventHandler:
    def __new__(cls, event_class: type[Event]):
        """Create a new EventHandler instance and add it to the Mediatr instance"""
        handlers_of_event = Mediatr.get_instance().handlers.get(event_class, [])
        current_handler_instance = super(EventHandler, cls).__new__(cls)

        handlers_of_event.append(current_handler_instance)
        Mediatr.get_instance().handlers[event_class] = handlers_of_event

        return current_handler_instance

    def __init__(self, event_class: type[Event]):
        self.event_class = event_class

    def handle(self, event: Event):
        raise NotImplementedError(
            "EventHandler subclasses must implement the handle method"
        )


class MoneyDepositedEventHandler(EventHandler):
    def __init__(self):
        super().__init__(MoneyDepositedEvent)

    def handle(self, event: MoneyDepositedEvent):
        logger.debug(
            f"""Handling MoneyDepositedEvent for account {event.data['account_id']} 
            with amount {event.data['amount']} and account amount {event.data['account_amount']}"""
        )


class MoneyWithdrawnEventHandler(EventHandler):
    def __init__(self):
        super().__init__(MoneyWithdrawnEvent)

    def handle(self, event: MoneyWithdrawnEvent):
        logger.debug(
            f"""Handling MoneyWithdrawnEvent for account {event.data['account_id']} 
            with amount {event.data['amount']} and account amount {event.data['account_amount']}"""
        )


class AccountCreatedEventHandler(EventHandler):
    def __init__(self):
        super().__init__(AccountCreatedEvent)

    def handle(self, event: AccountCreatedEvent):
        logger.debug(
            f"""Handling AccountCreatedEvent for account {event.data['account_id']}"""
        )


class EventStore:
    def __init__(self):
        self.store: dict[str, list[Event]] = {}

    def get_current_version(self, aggregate_id: str) -> int:
        """Versión que tendría el próximo evento para este agregado (derivada del store)."""
        return len(self.store.get(aggregate_id, []))

    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        if aggregate_id not in self.store:
            self.store[aggregate_id] = []
            
        current_version = self.get_current_version(aggregate_id)
        if current_version != expected_version:
            raise Exception("Concurrency error")

        for i, event in enumerate(events):
            event.version = current_version + i 

        # Save events in batch
        self.store.setdefault(aggregate_id, []).extend(events)

    def process_events(self, aggregate_id: str):
        for event in self.store.get(aggregate_id, []):
            logger.debug(f"Processing event {event.type} for aggregate {aggregate_id}")
            self.apply_event(aggregate_id, event)

    def apply_event(self, aggregate_id: str, event: Event):
        handlers = Mediatr.get_instance().handlers.get(type(event), [])


        for handler in handlers:
            handler.handle(event)
           


# Tarea: Implementar un agregado con Event Sourcing
class BankAccount:
    def __init__(self, account_id: str):
        self.id = account_id

        self.balance = 0
        self.version = 0
        self._pending_events = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.pending_events.append(
            MoneyDepositedEvent(
                self.id, amount, account_amount=self.balance
            )
        )
        self.version += 1
        logger.debug(
            f"Deposited {amount} to account {self.id}. New balance: {self.balance}"
        )

    def withdraw(self, amount: float) -> None:

        if self.balance < amount:
            raise Exception("Insufficient funds")
        self.balance -= amount
        self.pending_events.append(
            MoneyWithdrawnEvent(
                self.id, amount, account_amount=self.balance
            )
        )
        logger.debug(
            f"Withdrew {amount} from account {self.id}. New balance: {self.balance}"
        )

    @classmethod
    def from_store(cls, account_id: str, event_store: EventStore) -> "BankAccount":
        account = cls(account_id)
        event_store.process_events(account_id)
        return account
    
    @property
    def pending_events(self) -> List[Event]:
        return self._pending_events
