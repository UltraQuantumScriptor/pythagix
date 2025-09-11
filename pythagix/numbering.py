import math as m
from functools import lru_cache, reduce
import random
from timeit import timeit
from typing import List, Sequence, Set, Union
from pythagix.prime import is_prime

Numeric = Union[int, float]


def gcd(values: List[int]) -> int:
    """
    Compute the greatest common divisor (GCD) of a List of integers.

    Args:
        values (List[int]): A List of integers.

    Returns:
        int: The GCD of the numbers.

    Raises:
        ValueError: If the List is empty.
    """
    if not values:
        raise ValueError("Input List must not be empty")
    return reduce(m.gcd, values)


def lcm(values: List[int]) -> int:
    """
    Compute the least common multiple (LCM) of a List of integers.

    Args:
        values (List[int]): A List of integers.

    Returns:
        int: The LCM of the numbers.

    Raises:
        ValueError: If the List is empty.
    """
    if not values:
        raise ValueError("Input List must not be empty")

    return reduce(m.lcm, values)


@lru_cache(maxsize=None)
def get_factors(n: int) -> List[int]:
    """
    Return all positive factors of a number.

    Args:
        number (int): The number whose factors are to be found.

    Returns:
        List[int]: A sorted List of factors.

    Raises:
        ValueError: If the number is not positive.
    """
    if n <= 1:
        return []

    def is_probable_prime(n: int, k: int = 12) -> bool:
        """Miller–Rabin primality test."""
        return is_prime(n, k)

    def pollard_rho(n: int) -> int:
        """Pollard Rho with Brent's cycle detection."""
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        while True:
            y, c, block_size = (
                random.randrange(2, n - 1),
                random.randrange(1, n - 1),
                128,
            )
            g, r, q = 1, 1, 1
            x, ys = 0, 0
            while g == 1:
                x = y
                for _ in range(r):
                    y = (y * y + c) % n
                k = 0
                while k < r and g == 1:
                    ys = y
                    for _ in range(min(block_size, r - k)):
                        y = (y * y + c) % n
                        q = (q * abs(x - y)) % n
                    g = m.gcd(q, n)
                    k += block_size
                r *= 2
            if g == n:
                while True:
                    ys = (ys * ys + c) % n
                    g = m.gcd(abs(x - ys), n)
                    if g > 1:
                        break
            if g != n:
                return g

    # recursive factorization
    if is_probable_prime(n):
        return [n]
    d = pollard_rho(n)
    return get_factors(d) + get_factors(n // d)


@lru_cache(maxsize=None)
def compress_0(values: Sequence[Numeric]) -> List[Numeric]:
    """

    Clears consecutive zeros, Keeping only one of the zero.

    Args:
        values (Union(int, float)): A list of integers of float.

    Returns:
        List[int, float]: The given list with compressed zeros.
    """

    if len(values) <= 0:
        return []

    compressed = [values[0]]
    for i in range(1, len(values)):
        if values[i] == 0 and compressed[-1] == 0:
            continue
        compressed.append(values[i])

    return compressed


def nCr(n: int, k: int) -> Numeric:
    """
    Count all possible k items from n.

    Args:
        n (int): The number.
        k (int): The amount of items to choose from n
    """
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    return result
