from itertools import count
from typing import Iterable, Iterator, Tuple


def current_linux_user() -> str:
    """Returns current user name"""
    import os

    return os.getlogin()


def current_date() -> str:
    """Returns big-endian string of the current date"""
    import datetime

    return datetime.datetime.now().strftime("%Y-%m-%d")


def current_fqdn() -> str:
    """Returns fully-qualified domain main (FQDN) of current machine"""
    import socket

    return socket.getfqdn()


def as_range(iterable: Iterable[int]) -> str:
    """From https://codereview.stackexchange.com/q/5196
    If {iterable} has at least two elements, return '{first}-{last}', otherwise '{first}'.
    """
    items = list(iterable)
    if len(items) > 1:
        return f"{items[0]}-{items[-1]}"
    else:
        return f"{items[0]}"


def groupby_range(x: int, c: Iterator[int] = count()) -> int:
    return next(c) - x


def groupby_inverse_range(x: int, c: Iterator[int] = count()) -> int:
    return x - next(c)


def convert_to_largest_unit(
    value: float, unit: str, scale: float = 1000.0
) -> Tuple[float, str]:
    """Converts value to largest unit of the same type"""
    prefixes = ["", "k", "M", "G", "T", "P", "E", "Z", "Y"]
    current_scale = value
    prefix_index = 0
    for i, _ in enumerate(prefixes):
        if current_scale < scale:
            prefix_index = i
            break
        current_scale /= scale
    return current_scale, prefixes[prefix_index] + unit
