from functools import wraps
from types import FunctionType


def memoize(a_function: FunctionType) -> FunctionType:
    """A wrapper memoizationfunction for a function 
        that takes only 1 argument
    """
    # Implementing the cache dictionary
    _cache = {}

    @wraps(a_function)
    def inner(n: int):
        # Calculating the return value only if
        # it doesn't exist in the _cache dictionary
        if n not in _cache:
            _cache[n] = a_function(n)
        return _cache[n]

    # Making the caching mechanism available
    # as a function property
    inner.cache = _cache

    return inner


@memoize
def fibonacci(n: int) -> int:
    """A function that returns the passed
        Fibonacci sequence's index using recursion
    """
    if n < 3:
        return 1
    print(f"Calculating {n}!")
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonacci(10): {fibonacci(10)}\n")
print(f"Function's cache: {fibonacci.cache}\n")
print(f"Fibonacci(10) again (from cache!!!): {fibonacci(10)}\n")
print(f"Fibonacci(8) (from cache!!!): {fibonacci(8)}\n")
print(f"Fibonacci(15): {fibonacci(15)}\n")
