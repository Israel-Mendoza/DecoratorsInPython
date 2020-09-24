"""Using the wraps() decorator to avoid function metadata loss"""


from functools import wraps
from types import FunctionType
from typing import Any


def counter(a_func: FunctionType) -> FunctionType:
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count = 0

    # @wraps(function)    <- Alternative notation to line 19
    def inner(*args, **kwargs) -> Any:
        nonlocal count
        count += 1
        print(f"{a_func.__name__} has been called {count} times")
        return a_func(*args, **kwargs)

    # Transferring the metadata of the function to the closure using wraps
    inner = wraps(a_func)(inner)
    return inner


@counter
def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


print(add.__name__)  # Original name
print(add.__code__.co_freevars)
print(add.__closure__)
print(add.__annotations__)  # Correct annotations
help(add)  # Correct documentation, WRONG function signature
print()
