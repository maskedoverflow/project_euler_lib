import time

from eulerlib import consecutive_sum


def orgen():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


def subgen():
    return (sum(x for x in range(1000) if x % 3 == 0)
            + sum(x for x in range(1000) if x % 5 == 0)
            - sum(x for x in range(1000) if x % 15 == 0))


def submult():
    return (sum(3 * x for x in range(1000 // 3))
            + sum(5 * x for x in range(1000 // 5))
            - sum(15 * x for x in range(1000 // 15)))


def intelligent():
    return (consecutive_sum(3, 999, 3) + consecutive_sum(5, 999, 5)
            - consecutive_sum(15, 999, 15))


print(intelligent())
