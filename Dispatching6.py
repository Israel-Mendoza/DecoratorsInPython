"""Using the singledispatch decorator from the functools module"""

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape
from typing import Any


# Defining the default function to be called
# in case no type is found in the registry
@singledispatch
def htmlize(a: Any) -> str:
    """Returns a valid html string"""
    return escape(str(a))


@htmlize.register(Integral)
def html_integral(a: Integral) -> str:
    return f"{a}: {hex(a).upper()}"


@htmlize.register(Sequence)
def html_sequence(arg: Sequence) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{htmlize(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


"""ANALIZING THE htmlize DECORATED FUNCTION"""

print(type(htmlize.registry))
# <class 'mappingproxy'>

# What's in the registry dictionary?
print(htmlize.registry)
# {<class 'object'>: <function htmlize at 0x000002268FDBF040>,
# <class 'numbers.Integral'>: <function html_int at 0x00000226906AC3A0>,
# <class 'str'>: <function html_str at 0x00000226906AC4C0>,
# <class 'collections.abc.Sequence'>: <function html_list at 0x00000226906AC550>}

# What function will you use if I give you a string?
print(htmlize.dispatch(str))
# <function html_str at 0x00000226906AC4C0>

# What function will you use if I give you a boolean?
print(htmlize.dispatch(bool))
# <function html_integral at 0x0000013F0C0FB430>


"""Using decorated function"""

try:
    print(htmlize("1 < 10"))
except RecursionError as ex:
    print(f"{type(ex).__name__}: {ex}")
# RecursionError: maximum recursion depth exceeded while calling a Python object
# As no function for the type str has been registered, the function called will
# be that of the Sequence type, which calls htmlize for each item.
# Because each item of the string is also a string, htmlize will also be
# be called for that Sequence type. Thus, a RecursionError is raised.


# Implementing a function for the string type
@htmlize.register(str)
def html_str(arg: str) -> str:
    """
    Returns a string formated so it can
    be used as html code.
    """
    return escape(arg).replace("\n", "<br/>\n")


try:
    print(htmlize("1 < 10"))
    # 1 &lt; 10
except RecursionError as ex:
    print(f"{type(ex).__name__}: {ex}")
