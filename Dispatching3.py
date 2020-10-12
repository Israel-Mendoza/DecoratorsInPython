"""Introducing a decorator for dispatching - Part 1"""

from html import escape
from typing import Any, Callable


def single_dispatch(a_func: Callable) -> Callable:
    """
    Single dispatch decorator used with a function that
    takes 1 parameter.
    That function will be stored in the registry dictionary
    as the default function to be call when an object type
    instance is passed as arg to the returned closure.
    Cons:
        Unable to inject external functions.
    """
    registry = {}
    registry[object] = a_func

    def inner(arg: Any) -> Any:
        return registry[object](arg)

    inner.reg = registry
    return inner


"""Declaring a function"""


def htmlize(arg: Any) -> str:
    return escape(str(arg))


# Address of initial function.
print(hex(id(htmlize)).upper())
# 0X35C9340


"""Decorating and inspecting the function"""

# Decorating function
htmlize = single_dispatch(htmlize)

# Address of wrapped function.
print(hex(id(htmlize)).upper())
# 0X35C9388

# Analizing the closure
print(htmlize.__code__.co_freevars)
# ('registry',)
print(htmlize.__closure__)
# (<cell at 0x00EDF5C8: dict object at 0x00EF5E10>,)
print(hex(id(htmlize.reg[object])).upper())
# 0X35C9340 (Initial function is stored in the free variable)

"""Using decorated function"""

print(htmlize("a > b"))
# a &gt; b
