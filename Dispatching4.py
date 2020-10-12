"""Introducing a decorator for dispatching - Part 2"""

from html import escape
from typing import Callable


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
    registry[int] = lambda a: f"{a} ({hex(a)})"
    registry[str] = lambda a: escape(a).replace("\n", "<br/>\n")

    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    return inner


"""Declaring a function"""


@single_dispatch
def htmlize(arg):
    return escape(str(arg))


print(htmlize("AT&T"))
# AT&amp;T  // Str was hardcoded in decorator
print(htmlize(10))
# 10 (0xa)  // Int was hardcoded in decorator
print(htmlize([1, 2, 3]))
# [1, 2, 3] // list type was not hardcoded in decorator
