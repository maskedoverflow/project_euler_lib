def factorize_odd(n):
    if not isinstance(n, int):
        raise TypeError
    if n % 2 == 0:
        yield 2
    for x in range(3, int(n ** .5), 2):
        if n % x == 0:
            yield x
            reverse = n // x
            if reverse != x:
                yield n // x


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError
    if n & 1 == 0:
        return True
    for x in range(3, int(n ** .5), 2):
        if n % x == 0:
            return False
    return True


def prime_factors(n):
    if not isinstance(n, int):
        raise TypeError
    return {x for x in factorize_odd(n) if is_prime(x)}


factors = prime_factors(600851475143)
print(max(factors))
