"""Decorator factories with functions and classes"""


from functools import wraps
from types import FunctionType
from typing import Any

# Simple decorator factory


def simple_decorator(a: int, b: int) -> FunctionType:
    """Decorator factory"""
    def _simple_decorator(a_func: FunctionType) -> FunctionType:
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}" where a={a} and b={a}')
            return a_func(*args, **kwargs)
        return inner
    return _simple_decorator


# Replicating the above using a class


class SimpleDecorator:
    """Decorator factory"""

    def __init__(self, a: int, b: int):
        """Initialized the desired "free variables" that self will store"""
        self._a = a
        self._b = b

    def __call__(self, a_func: FunctionType) -> FunctionType:
        """
        Using __call__ as a decorator.
        When a SimpleDecorator instance is called,
        it returns a decorated function.
        Args:
            a_func [FunctionType] : Function to be decorated
        Returns:
            a_func decorated
        """
        @wraps(a_func)
        def simple_decorator(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}": a={self._a} and b={self._b}')
            return a_func(*args, **kwargs)
        return simple_decorator


@simple_decorator(10, 20)
def say_hello(name: str) -> None:
    print(f"Hello, {name}!\n")


@SimpleDecorator(100, 200)
def say_bye(name: str) -> None:
    print(f"Goodbye, {name}!\n")


say_hello("Israel")
say_bye("Israel")


print(say_hello.__name__)  # Original name due to wraps()
print(say_hello.__code__.co_freevars)  # ('a', 'a_func')
print(say_hello.__closure__)  # (<cell for int>, <cell for function>)
print(say_hello.__annotations__)  # Original annotations
help(say_hello)  # Original metadata due to wraps()
print()

print(say_bye.__name__)  # Original name due to wraps()
print(say_bye.__code__.co_freevars)
# ('a', 'self') // self is the SimpleDecorator instance
print(say_bye.__closure__)
# (<cell for function>, <cell for SimpleDecorator object>)
print(say_bye.__annotations__)  # Original annotations
help(say_bye)  # Original metadata due to wraps()
print()
