from functools import reduce


def consecutive_sum(min, max=None, diff=1):
    """Return sum of numbers from min to max, with step size diff.

    diff defaults to 1.

    If only one argument is given, it is assumed to be the maximum.
    In that case, min defaults to 1.
    """
    if (not isinstance(min, int) or not (isinstance(max, int) or max is None)
        or not isinstance(diff, int)):
         raise TypeError("Arguments must be int")
    if max is None:
        max = min
        min = 1
        n_elems = max
    else:
        n_elems = (max - min) // diff + 1
    return int((n_elems) * (min + diff * (n_elems - 1) / 2))


def fibonacci():
    """Create a generator which returns consecutive Fibonacci numbers."""
    last = 0
    current = 1
    while True:
        yield current
        last, current = current, last + current


def segment_reduce(function, iterable, seglen):
    """Combine stretches of length seglen using the given function.

    This function returns an iterator that contains all totals of
    combining stretches of length seglen in the given iterable.
    """
    l = list(iterable)
    return iter((reduce(function, l[i:i + seglen]) for i in range(0, len(l) - (seglen - 1))))


def transpose(array):
    """Transpose multidimensional array."""
    return list(map(list, zip(*array)))


def rotate(array):
    """Rotate multidimensional array by 90 degrees clockwise."""
    return list(map(list, zip(*reversed(array))))
