from functools import wraps, reduce
from types import FunctionType
from time import perf_counter


def function_timer(fn: FunctionType) -> FunctionType:
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
# Using a loop
@function_timer
def loop_fibonacci(n: int) -> list:
    n = abs(n)
    if n == 0:
        raise ValueError("Number of Fibonacci value must be other than zero")
    current_num = 1
    new_number = 1
    while n != 1:
        new_number, current_num = new_number + current_num, new_number
        n -= 1
    return current_num


######################################################################################


def _recursive_fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return _recursive_fibonacci(n - 1) + _recursive_fibonacci(n - 2)


# Avoiding innecesary calls to the decorator in recursive function
@function_timer
def recursive_fibonacci(n: int) -> int:
    return _recursive_fibonacci(n)


######################################################################################

# Using the reduce function
@function_timer
def reduce_fibonacci(n: int) -> int:
    initial_tuple = (0, 1)
    dummy = range(n)
    # n will never be used in the function
    fib_n = reduce(lambda prev, n: (prev[1], prev[0] + prev[1]), dummy, initial_tuple)
    return fib_n[0]


print(reduce_fibonacci(1000), end="\n\n")
print(loop_fibonacci(1000), end="\n\n")
# Using the recursive
print(recursive_fibonacci(10))
