"""Introducing decorators"""


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
    # Return the closure
    return inner


"""Implementing the decorator with traditional and @ notation"""


def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


add = counter(add)


@counter
def sub(x: int, y: int) -> int:
    """Returns the substraction of the passed integers"""
    return x - y


"""ORIGINAL METADATA IS LOST. INNER'S WILL BE DISPLAYED"""

print(add.__name__)  # "inner" because of the closure
print(add.__code__.co_freevars)  # ('a_func', 'count')
print(add.__closure__)  # (<cell for function>, <cell for int>)
print(add.__annotations__)  # Annotations dictionary from "inner"
help(add)  # Metadata of "inner" because of the closure
print()

print(sub.__name__)  # "inner" because of the closure
print(sub.__code__.co_freevars)  # ('a_func', 'count')
print(sub.__closure__)  # (<cell for function>, <cell for int>)
print(sub.__annotations__)  # Annotations dictionary from "inner"
help(sub)  # Metadata of "inner" because of the closure
print()

"""Using the decorated functions"""

print(add(10, 20))  # add has been called 1 times -> 30
print(add(20, 30))  # add has been called 2 times -> 50
print(add(30, 40))  # add has been called 3 times -> 70
print()
print(sub(10, 20))  # sub has been called 1 times -> -10
print(sub(20, 30))  # sub has been called 2 times -> -10
print(sub(30, 40))  # sub has been called 3 times -> -10
