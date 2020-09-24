"""Stacked decorators breakdown"""


from typing import Any
from types import FunctionType
from functools import wraps

# Stacking decorators


def decorator_1(a_func: FunctionType) -> FunctionType:
    @wraps(a_func)
    def inner(*args, **kwargs) -> Any:

        result = a_func(*args, **kwargs)
        print("Running decorator 1!")
        return result
    return inner


def decorator_2(a_func: FunctionType) -> FunctionType:
    @wraps(a_func)
    def inner(*args, **kwargs) -> Any:

        result = a_func(*args, **kwargs)
        print("Running decorator 2!")
        return result
    return inner


def simple_function(name: str) -> None:
    """Simple function that greets the passed name"""
    print(f"Hello, {name}!")


# Decorating the simple_function function with decorator_2
simple_function_1 = decorator_1(simple_function)
# Decorating the decorated function with decorator_1
simple_function_1 = decorator_2(simple_function_1)

# Another way of decorating the function:
simple_function_2 = decorator_2(decorator_1(simple_function))

# Another way of decorating the function:


@decorator_2
@decorator_1
def simple_function_3(name: str) -> None:
    """Simple function that greets the passed name"""
    print(f"Hello, {name}!")


# Running all three decorated functions
simple_function_1("Israel")
# Running decorator 1!
# Running decorator 2!
# Hello, Israel!
simple_function_2("Israel")
# Running decorator 1!
# Running decorator 2!
# Hello, Israel!
simple_function_3("Israel")
# Running decorator 1!
# Running decorator 2!
# Hello, Israel!
