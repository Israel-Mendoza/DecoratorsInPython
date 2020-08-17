import pytz
from datetime import datetime
from types import FunctionType
from functools import wraps


def function_logger(a_function: FunctionType) -> FunctionType:
    @wraps(a_function)
    def logger(*args, **kwargs):
        run_datetime = datetime.now(pytz.UTC)
        result = a_function(*args, **kwargs)
        _args = list(args)
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        all_args = tuple(_args + _kwargs)
        print(f"{run_datetime}: called '{a_function.__name__}({all_args})'")
        return result

    return logger


@function_logger
def fibonacci(n):
    """A Fibonacci number generator, using recursion"""
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Using the decorated function on a fibonacci recursive function,
# which shows the need of a caching system (multiple repeted calculations generated).
# print(fibonacci(12))


# Implementing a dictionary as a chaching mechanism


class FibonacciWrapper:
    """
    A class intended to wrap a fibonacci function.
    Implements a caching mechanism as a memoization system
    """

    def __init__(self):
        # Initialized some well-known values for the Fibonacci sequence
        self.cache = {1: 1, 2: 1}

    def __call__(self, n: int) -> int:
        # Calculating the fibonacci result
        # _only_ if it doen't exists in the self.cache dictionary
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self(n - 1) + self(n - 2)
        # Returning the cached result
        return self.cache[n]


f1 = FibonacciWrapper()
print(f1(10))
print(type(f1))  # f1 is a FibonacciWrapper callable object
# Accessing the caching dictionary
print(f"Cache dictionary: {f1.cache}")


# Recreating the previous examples with closures


def fibonacci_recursive() -> FunctionType:
    """
    A decorator intended to wrap a fibonacci function.
    Implements a caching mechanism as a memoization system
    """
    # Initialized some well-known values for the Fibonacci sequence
    _cache = {1: 1, 2: 1}

    def inner(n: int):
        # Calculating the fibonacci result
        # _only_ if it doen't exists in the _cache dictionary
        if n not in _cache:
            print(f"Calculating fibonacci({n})")
            _cache[n] = inner(n - 1) + inner(n - 2)
        # Returning the cached result
        return _cache[n]

    # Making the _cache dictionary available through an interface
    inner.cache = _cache

    return inner


f2 = fibonacci_recursive()
print(f2(10))
print(type(f2))  # f1 is a function
# Accessing the caching dictionary
print(f"Cache dictionary: {f2.cache}")
