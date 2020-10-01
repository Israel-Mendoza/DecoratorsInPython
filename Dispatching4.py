"""Introducing a decorator for dispatching"""

from types import FunctionType
from html import escape


def single_dispatch(a_func: FunctionType) -> FunctionType:
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
# AT&amp;T
print(htmlize(10))
# 10 (0xa)
print(htmlize([1, 2, 3]))
# [1, 2, 3]
