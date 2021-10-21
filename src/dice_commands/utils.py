
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
