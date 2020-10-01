"""Making a case use for dispatching"""

from html import escape
from typing import Any

"""Creating functions that will be then dispatch by another function"""


def html_escape(arg):
    return escape(str(arg))


def html_str(arg: Any) -> str:
    """
    Returns a string formated so it can
    be used as html code.
    """
    return html_escape(arg).replace("\n", "<br/>\n")


def html_int(arg: Any) -> str:
    """
    Returns a string containing the int and it's
    hex representation.
    """
    return f"{arg} ({hex(arg)})"


def html_list(arg: Any) -> str:
    """
    Returns a string where each item is wrapped in a 
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{html_format(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


def html_dict(arg):
    """
    Returns a string where each key-value pair 
    is wrapped in a <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{k}: {html_format(v)}</li>" for k, v in arg.items())
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


def html_float(arg: float) -> str:
    """
    Returns a string containing the float
    formated to contain 2 decimals.
    """
    return f'{arg:.2f}'


"""Creating a dispatch function using a registry dictionary"""


def html_format(arg: Any) -> str:
    """
    Dispatcher function:
    Cons:
        Hard coded registry, difficult to modify from the outside.
    """
    registry = {
        object: html_escape,
        str: html_str,
        int: html_int,
        float: html_float,
        list: html_list,
        tuple: html_list,
        dict: html_dict
    }

    return registry.get(type(arg), registry[object])(arg)


a = [
    """Company:
    Steinway & Sons
    """,
    (1, 2, 3),
    100,
    {"uno": "un", "dos": "deux", "tres": "trois"}
]

print(html_format(a))
