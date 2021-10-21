from collections.abc import Iterable


def current_linux_user() -> str:
    """Returns current user name"""
    import os
    return os.getlogin()


def current_date() -> str:
    """Returns big-endian string of the current date"""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d")


def current_fqdn() -> str:
    """ Returns fully-qualified domain main (FQDN) of current machine"""
    import socket
    return socket.getfqdn()


def as_range(iterable: Iterable) -> str:
    """From https://codereview.stackexchange.com/q/5196
    If {iterable} has at least two elements, return '{first}-{last}', otherwise '{first}'.
    """
    l = list(iterable)
    if len(l) > 1:
        return "{0}-{1}".format(l[0], l[-1])
    else:
        return "{0}".format(l[0])
