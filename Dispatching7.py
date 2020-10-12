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
def _(a: Integral) -> str:
    return f"{a}: {hex(a).upper()}"


@htmlize.register(Sequence)
def _(arg: Sequence) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{htmlize(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


@htmlize.register(str)
def _(arg: str) -> str:
    """
    Returns a string formated so it can
    be used as html code.
    """
    return escape(arg).replace("\n", "<br/>\n")


"""ANALIZING THE htmlize DECORATED FUNCTION"""

# Python doesn't care about the name of the wrapped functions.
# It only looks at the address where these functions live.
# Remember that names are only labels.

# What's in the registry dictionary?
print(htmlize.registry)
# {<class 'object'>: <function htmlize at 0x0000027ED7A6F040>,
# <class 'numbers.Integral'>: <function _ at 0x0000027ED7FFB430>,
# <class 'collections.abc.Sequence'>: <function _ at 0x0000027ED7FFB4C0>,
# <class 'str'>: <function _ at 0x0000027ED7FFB550>}


# What function will you use if I give you a string?
print(htmlize.dispatch(str))
# <function _ at 0x0000027ED7FFB550>

# What function will you use if I give you a boolean?
print(htmlize.dispatch(bool))
# <function _ at 0x0000027ED7FFB430> // Notice different address
