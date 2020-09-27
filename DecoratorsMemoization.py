"""Introducing memoization"""


import pytz
from typing import Any
from datetime import datetime
from types import FunctionType
from functools import wraps


def function_logger(a_function: FunctionType) -> FunctionType:
    """Function decorator"""
    @wraps(a_function)
    def logger(*args, **kwargs) -> Any:
        """
        Wrapper function.
        Prints information about the time and arguments the
        wrapped function is called.
        """
        # Capturing time the function is called
        run_datetime = datetime.now(pytz.UTC)
        # Storing the result of the called wrapped function
        result = a_function(*args, **kwargs)
        # Capturing the arguments in a tuple
        _args = [str(arg) for arg in args]
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        _args = ", ".join(_args)
        _kwargs = ", ".join(_kwargs)
        all_args = _args + _kwargs
        # Printing the information
        print(f"{run_datetime}: called '{a_function.__name__}({all_args})'")
        # Returning the wrapped function's result
        return result
    # Returning the wrapped function
    return logger


# Using the decorated function on a fibonacci recursive function
@function_logger
def fibonacci(n):
    """A Fibonacci number generator, using recursion"""
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
Calling a decorated recursive function. 
Calculations are duplicated, which can be expensive.
"""

# Notice how fibonacci(2) gets calculated up to 4 times
# when calling fibonacci(6)!!!
# print(fibonacci(6))
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' 
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(4)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (2)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)' -> Already calculated
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)' -> Already calculated
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(5)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (3)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)' -> Already calculated (2)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)' -> Already calculated (2)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (4)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(4)' -> Already calculated
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(6)'
# 8


"""
Implementing dictionaries in a class as a chaching 
mechanisms to prevent inecessary calculations.
"""


class FibonacciClass:
    """
    A class that contains a fibonacci calculator.
    Class instance is callable, which is the fibonacci calculator.
    Implements a caching mechanism as a memoization system
    to avoid duplicated calculations.
    """
    def __init__(self):
        """
        Initializing the caching mechanism containing
        known values for fibonacci(1) and fibonacci(2).
        """
        self.cache = {1: 1, 2: 1}

    def __call__(self, n: int) -> int:
        """
        When the class instance is called, it calculates
        fibonnaci(n).
        First, it looks for the existing cached value;
        if found, returned, if not, calculates it and
        stores it in the cache dictionary.
        """
        if n not in self.cache:
            # Prints the object calling only wheb
            # values are calculated
            print(f"Calculating fib({n})")
            self.cache[n] = self(n - 1) + self(n - 2)
        # Returning the cached result
        return self.cache[n]


# Creating a FibonacciClass instance
f1 = FibonacciClass()

# Notice how there are no duplicated calculations
print(f1(10))
# Calculating fib(10)
# Calculating fib(9)
# Calculating fib(8)
# Calculating fib(7)
# Calculating fib(6)
# Calculating fib(5)
# Calculating fib(4)
# Calculating fib(3)

print(type(f1))  # <class '__main__.FibonacciClass'>

# Accessing the caching dictionary
print(f1.cache) 
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}


"""
Implementing dictionaries in a class as a chaching 
mechanisms to prevent inecessary calculations.
"""


def fibonacci_function() -> FunctionType:
    """
    Returns a fibonacci calculator function.
    Returned function implements a caching dictionary 
    as a memoization mechanism.
    """
    #Initializing the caching mechanism containing
    # known values for fibonacci(1) and fibonacci(2).
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


# Storing the returned function from 
# "fibonacci_function" to f2
f2 = fibonacci_function()

# Notice how there are no duplicated calculations
print(f2(10))
# Calculating fibonacci(10)
# Calculating fibonacci(9)
# Calculating fibonacci(8)
# Calculating fibonacci(7)
# Calculating fibonacci(6)
# Calculating fibonacci(5)
# Calculating fibonacci(4)
# Calculating fibonacci(3)

print(type(f2))  # <class 'function'>

# Accessing the caching dictionary
print(f2.cache)
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
