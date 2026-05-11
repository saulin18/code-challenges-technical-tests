# Your goal is to write an Event constructor function, which can be used to make event objects.

# An event object should work like this:

# it has a .subscribe() method, which takes a function and stores it as its handler
# it has an .unsubscribe() method, which takes a function and removes it from its handlers
# it has an .emit() method, which takes an arbitrary number of arguments and calls all the 
# stored functions with these arguments

from typing import Callable


class Event():
    def __init__(self) -> None:
        self.handlers: list[Callable] = []

    def subscribe(self, handler: Callable) -> None:
        self.handlers.append(handler)

    def unsubscribe(self, handler: Callable) -> None:
        self.handlers.remove(handler)

    def emit(self, *args, **kwargs) -> None:
        for handler in self.handlers:
            handler(*args, **kwargs)