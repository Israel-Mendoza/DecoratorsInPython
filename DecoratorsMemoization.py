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
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(12))

# Caching calculated results in a dictionary


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def __call__(self, n: int) -> int:
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self(n - 1) + self(n - 2)
        return self.cache[n]


f1 = Fib()
print(f1(10))
print(f"Cache dictionary: {f1.cache}")


# Recreating the previous examples with closures


def fibonacci_recursive() -> FunctionType:
    _cache = {1: 1, 2: 1}

    def inner(n: int):
        if n not in _cache:
            print(f"Calculating fibonacci({n})")
            _cache[n] = inner(n - 1) + inner(n - 2)
        return _cache[n]

    inner.cache = _cache

    return inner


f2 = fibonacci_recursive()
print(f2(10))
print(f"Cache dictionary: {f2.cache}")
