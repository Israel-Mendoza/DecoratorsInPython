"""Decorator factories or parameterized decorators"""


from time import perf_counter
from functools import wraps
from types import FunctionType
from typing import Any


def function_timer(n: int) -> FunctionType:
    """Decorator factory"""
    def _function_timer(a_func: FunctionType) -> FunctionType:
        """
        Decorator function. Returns a closure that, when called,
        will print on the screen the function call representation
        and the time it took to run.
        """
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            # Start with zero time
            total_elapsed = 0
            # Loop n times (n is free variable passed to function_timer)
            for i in range(n):
                start = perf_counter()
                # Store the return from the wrapped function
                result = a_func(*args, **kwargs)
                # Add the elapsed time to the total_elapsed free variable
                total_elapsed += perf_counter() - start
            # Calculating the average time
            avg_elapsed_time = total_elapsed / 10
            # Capture args and kwargs in a string
            _args = list(args)
            _kwargs = [f"{k}={v}" for k, v in kwargs.items()]
            _args.extend(_kwargs)
            _args = str(args)
            func_call_str = f"{a_func.__name__}{_args}"
            # Print calling information
            print(f"{func_call_str} ran {n} times")
            print(f"{func_call_str} took in average {avg_elapsed_time:.6f}s")
            # Return result from calling wrapped function
            return result
        # Returning decorated function
        return inner
    # Returing decorator function
    return _function_timer


@function_timer(10000000)
def add(x: int, y: int) -> int:
    return x + y


# add = function_timer(10000)(add) // Traditional notation


print(add.__code__.co_freevars)  # ('a_func', 'n')
print(add.__closure__)  # (<cell to function>, <cell to int)
add(10, 20)
# add(10, 20) ran 100000 times
# add(10, 20) took in average 0.011496s
