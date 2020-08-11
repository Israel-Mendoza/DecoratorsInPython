import pytz
from types import FunctionType
from functools import wraps
from datetime import datetime


# Using Decorators as loggers


def function_logger(a_function: FunctionType) -> FunctionType:
    """
    Decorator function. Returns a closure that, when called,
    will print the time the function was called and a function
    call representation.
    """

    @wraps(a_function)
    def logger(*args, **kwargs):
        run_datetime = datetime.now(pytz.UTC)
        result = a_function(*args, **kwargs)
        _args = list(args)
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        all_args = tuple(_args + _kwargs)
        print(f"{run_datetime}: called '{a_function.__name__}{all_args}'")
        return result

    return logger


@function_logger
def func1(a, b, c=10):
    pass


@function_logger
def func2():
    pass


func1(2, 5)
func2()
