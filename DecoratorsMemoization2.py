"""Memoizing any function using a decorator"""


from functools import wraps
from types import FunctionType


def memoize(a_function: FunctionType) -> FunctionType:
    """
    A wrapper memoization function for a 
    function that takes only 1 argument.
    """
    # Implementing the cache dictionary
    _cache = {}

    @wraps(a_function)
    def inner(n: int):
        """
        Calculating the return value only if
        it doesn't exist in the _cache dictionary
        """
        if n not in _cache:
            _cache[n] = a_function(n)
        return _cache[n]

    # Making the caching mechanism available
    # as a function property
    inner.cache = _cache

    return inner


@memoize
def fibonacci(n: int) -> int:
    """
    A function that returns the passed
    Fibonacci sequence's index using recursion
    """
    if n < 3:
        return 1
    print(f"Calculating {n}!")
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
# Calculating 10!
# Calculating 9!
# Calculating 8!
# Calculating 7!
# Calculating 6!
# Calculating 5!
# Calculating 4!
# Calculating 3!

print(fibonacci.cache)
# {2: 1, 1: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}

# Calculating fibonacci(10) again
# Notice how value is taken from caching dictionary
print(fibonacci(10))
# 55

print(f"Fibonacci(8) (from cache!!!): {fibonacci(8)}\n")
# Fibonacci(8) (from cache!!!): 21

print(f"Fibonacci(15): {fibonacci(15)}\n")
# Calculating 15!
# Calculating 14!
# Calculating 13!
# Calculating 12!
# Calculating 11!
# Fibonacci(15): 610
