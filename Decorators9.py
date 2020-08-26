from functools import wraps
from types import FunctionType
from typing import Any

# Simple decorator factory


def simple_decorator(a: int, b: int) -> FunctionType:
    def _simple_decorator(a_func: FunctionType) -> FunctionType:
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}" where a={a} and b={a}')
            return a_func(*args, **kwargs)

        return inner

    return _simple_decorator


# Replicating the above using a class


class SimpleDecorator:
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b

    def __call__(self, a_func: FunctionType) -> FunctionType:
        def inner(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}" where a={self._a} and b={self._b}')
            return a_func(*args, **kwargs)

        return inner


@simple_decorator(10, 20)
def say_hello(name: str) -> None:
    print(f"Hello, {name}!\n")


@SimpleDecorator(100, 200)
def say_bye(name: str) -> None:
    print(f"Goodbye, {name}!\n")


say_hello("Israel")
say_bye("Israel")
