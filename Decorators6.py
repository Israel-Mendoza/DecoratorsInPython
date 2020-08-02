import pytz
from types import FunctionType
from time import perf_counter
from datetime import datetime
from functools import wraps, reduce


def function_timer(fn: FunctionType) -> FunctionType:
    @wraps(fn)
    def inner_func(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        _args = [str(a) for a in args]
        _kwargs = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = _args + _kwargs
        all_args = ", ".join(all_args)
        print(f"{fn.__name__}({all_args}) took {elapsed:.6f} seconds to run.")
        return result

    return inner_func


def function_logger(a_function):
    @wraps(a_function)
    def logger(*args, **kwargs):
        run_datetime = datetime.now(pytz.UTC)
        result = a_function(*args, **kwargs)
        _args = list(args)
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        all_args = list(_args + _kwargs)
        print(f"{run_datetime}: called '{a_function.__name__}({all_args})'")
        return result

    return logger


@function_logger
@function_timer
def factorial_recursive(n):
    return _factorial(n)


def _factorial(n):
    if n == 1:
        return 1
    return n * _factorial(n - 1)


@function_logger
@function_timer
def factorial_loop(n):
    result = n
    while n > 1:
        result = result * (n - 1)
        n -= 1
    return result


@function_logger
@function_timer
def factorial_reduced(n):
    result = reduce(lambda x, y: x * y, range(1, n + 1))
    return result


print(factorial_recursive(100))
print(factorial_loop(100))
print(factorial_reduced(100))
