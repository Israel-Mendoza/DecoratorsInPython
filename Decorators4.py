from functools import wraps, reduce
from types import FunctionType
from time import perf_counter


def function_timer(fn: FunctionType) -> FunctionType:
    """
    Decorator function. Wraps a function, and prints
    the time the function took to run and the password arguments.
    Returned function keeps wrapped function's signature
    """
    # Using the wraps() decorator to keep wrapped function signature
    @wraps(fn)
    def closure(*args, **kwargs):
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

    return closure


######################################################################################
# Decorating a fibonacci function using a loop
@function_timer
def loop_fibonacci(n: int) -> list:
    # Getting rid of negative values
    n = abs(n)
    if n == 0:
        raise ValueError("Number of Fibonacci value must be other than zero")
    current_num = 0
    new_number = 1
    while n != 1:
        new_number, current_num = new_number + current_num, new_number
        n -= 1
    return new_number


######################################################################################


# Avoiding innecesary calls to the decorator in recursive function
# by wrapping the recursive function in another function
@function_timer
def recursive_fibonacci(n: int) -> int:
    # Getting rid of negative numbers
    if n == 0:
        raise ValueError("Number of Fibonacci value must be other than zero")
    n = abs(n)

    def _recursive_fibonacci(n: int) -> int:
        # Fibonacci of 1 and 2 = 1
        if n < 3:
            return 1
        return _recursive_fibonacci(n - 1) + _recursive_fibonacci(n - 2)

    return _recursive_fibonacci(n)


######################################################################################

# Using the reduce function
@function_timer
def reduce_fibonacci(n: int) -> int:
    # Setting an initial tuple
    # Index 0 is the previous number and index 1 is the new value
    initial_tuple = (0, 1)
    # A dummy number generator to keep the reduce function running
    dummy = range(n)
    # n will receive the number from the dumy. It won't be used in the function
    fib_n = reduce(lambda prev, n: (prev[1], prev[0] + prev[1]), dummy, initial_tuple)
    return fib_n[0]


# Testing all three decorated functions
print(reduce_fibonacci(8), end="\n\n")
print(loop_fibonacci(8), end="\n\n")
print(recursive_fibonacci(8))
