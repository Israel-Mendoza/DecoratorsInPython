"""Working on stacked decorators"""


import pytz
from types import FunctionType
from typing import Any
from time import perf_counter
from datetime import datetime
from functools import wraps, reduce


"""Implementing decorators"""


def function_timer(a_func: FunctionType) -> FunctionType:
    """
    Decorator function. Returns a closure that, when called,
    will print on the screen the function call representation
    and the time it took to run.
    """
    @wraps(a_func)
    def inner_func(*args, **kwargs) -> Any:
        # Capturing execution time
        start = perf_counter()
        # Running function and storing return value
        result = a_func(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        # Capturing args and kwargs in a string
        _args = [str(a) for a in args]
        _kwargs = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = _args + _kwargs
        all_args = ", ".join(all_args)
        # Print timing information
        print(f"{a_func.__name__}({all_args}) took {elapsed:.6f} seconds to run.")
        return result

    return inner_func


def function_logger(a_func: FunctionType) -> FunctionType:
    """
    Decorator function. Returns a closure that, when called,
    will print the time the function was called and a function
    call representation.
    """
    @wraps(a_func)
    def logger(*args, **kwargs):
        # Capturing date and time object when wrapped function is called
        run_datetime = datetime.now(pytz.UTC)
        # Running function and storing its return value
        result = a_func(*args, **kwargs)
        _args = list(args)
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        # Capturing args and kwargs in a tuple
        all_args = list(_args + _kwargs)
        # Printing logger info (to stdout but could be log server)
        print(f"{run_datetime}: called '{a_func.__name__}({all_args})'")
        return result
    return logger


"""Stacking decorators"""


@function_logger  # To run second
@function_timer  # To run first
def factorial_recursive(n):
    def _factorial(n):
        if n == 1:
            return 1
        return n * _factorial(n - 1)
    return _factorial(n)


@function_logger  # To run second
@function_timer  # To run first
def factorial_loop(n):
    result = n
    while n > 1:
        result = result * (n - 1)
        n -= 1
    return result


@function_logger  # To run second
@function_timer  # To run first
def factorial_reduced(n):
    result = reduce(lambda x, y: x * y, range(1, n + 1))
    return result


"""Testing decorated functions"""

print(factorial_recursive(10))
# factorial_recursive(10) took 0.000006 seconds to run.
# 2020-09-24 03:47:18.957479+00:00: called 'factorial_recursive([10])'
# -> 3628800

print(factorial_loop(10))
# factorial_loop(10) took 0.000003 seconds to run.
# 2020-09-24 03:47:18.957479+00:00: called 'factorial_loop([10])'
# -> 3628800

print(factorial_reduced(10))
# factorial_reduced(10) took 0.000005 seconds to run.
# 2020-09-24 03:47:18.957479+00:00: called 'factorial_reduced([10])'
# -> 3628800
