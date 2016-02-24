import traceback


def sum(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError
    if not a >= 0 or not b >= 0:
        raise ValueError
    else:
        return int(a) + int(b)