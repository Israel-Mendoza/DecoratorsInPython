from time import perf_counter
from functools import wraps
from types import FunctionType


def function_timer(n: int):
    def _function_timer(fn: FunctionType):
        """
        Decorator function. Returns a closure that, when called,
        will print on the screen the function call representation
        and the time it took to run.
        """

        @wraps(fn)
        def inner(*args, **kwargs):
            # Start with zero time
            total_elapsed = 0
            # Loop n times
            for i in range(n):
                start = perf_counter()
                # Store the return from the wrapped function
                result = fn(*args, **kwargs)
                # Add the elapsed time to the total_elapsed free variable
                total_elapsed += perf_counter() - start
            # Calculating the average time
            avg_elapsed_time = total_elapsed / 10
            # Store all args un kwargs as a string
            _args = list(args)
            _kwargs = [f"{k}={v}" for k, v in kwargs.items()]
            _args.extend(_kwargs)
            _args = str(args)
            func_call_str = f"{fn.__name__}{_args}"
            print(f"{func_call_str} ran {n} times")
            print(f"{func_call_str} took in average {avg_elapsed_time:.6f}s")
            return result

        return inner

    return _function_timer


@function_timer(2)
def add(x, y):
    for i in range(1):
        result = x + y
    return i


add(10, 20)
