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


"""Creating a dispatch function"""


def html_format(arg: Any) -> str:
    """Dispatcher function"""
    if isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float):
        return html_float(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)


a = [
    """Company:
    Steinway & Sons
    """,
    (1, 2, 3),
    100,
    {"uno": "un", "dos": "deux", "tres": "trois"}
]

print(html_format(a))
# <ul>
# 	<li>Hello<br/>
# Fucking<br/>
# Bitches<br/>
# </li>
# 	<li><ul>
# 	<li>1 (0x1)</li>
# 	<li>2 (0x2)</li>
# 	<li>3 (0x3)</li>
# </ul></li>
# 	<li>100 (0x64)</li>
# 	<li><ul>
# 	<li>uno: un</li>
# 	<li>dos: deux</li>
# 	<li>tres: trois</li>
# </ul></li>
# </ul>
