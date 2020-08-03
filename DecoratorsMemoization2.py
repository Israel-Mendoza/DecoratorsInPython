from functools import wraps
from types import FunctionType


def memoize(a_function) -> FunctionType:
    _cache = {}

    @wraps(a_function)
    def closure(n: int):
        if n not in _cache:
            _cache[n] = a_function(n)
        return _cache[n]

    closure.cache = _cache

    return closure


@memoize
def fibonacci(n: int) -> int:
    if n < 3:
        return 1
    print(f"Calculating {n}!")
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonacci(10): {fibonacci(10)}\n")
print(f"Function's cache: {fibonacci.cache}\n")
print(f"Fibonacci(10) again (from cache!!!): {fibonacci(10)}\n")
print(f"Fibonacci(8) (from cache!!!): {fibonacci(8)}\n")
print(f"Fibonacci(15): {fibonacci(15)}\n")
