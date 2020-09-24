"""Attempt not to lose the original funtion's metadata"""


from types import FunctionType
from typing import Any


# Defining the decorator function
def counter(a_func: FunctionType) -> FunctionType:
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal count  # Free variable from outer scope
        count += 1
        print(f"{a_func.__name__} has been called {count} times")
        # Return wrapped function return value when called with passed args
        return a_func(*args, **kwargs)

    # Transferring the metadata of the function to the closure
    inner.__name__ = a_func.__name__
    inner.__doc__ = a_func.__doc__
    inner.__annotations__ = a_func.__annotations__
    return inner


@counter
def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


print(add.__name__)  # Original name
print(add.__code__.co_freevars)  # ('a_func', 'count')
print(add.__closure__)  # (<cell to function>, <cell to int>)
print(add.__annotations__)  # Original annotations
help(add)  # Correct name and documentation. WRONG function signature
print()
