import math as m
from functools import lru_cache, reduce
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
def get_factors(number: int) -> List[int]:
    """
    Return all positive factors of a number.

    Args:
        number (int): The number whose factors are to be found.

    Returns:
        List[int]: A sorted List of factors.

    Raises:
        ValueError: If the number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive")

    factors: Set[int] = set()
    for i in range(1, m.isqrt(number) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)


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


def prime_factorization(number: int) -> Union[List[int], None]:
    """
    Find all prime factors of the given number.

    Args:
        number (int): The number whose factors are to be found.

    Returns:
        Union[List[int], None]: The prime factors found for number. returns
        None if the number is prime.
    """
    if is_prime(number):
        return None
    n = 2
    result = []
    while number > 1:

        if n > number:
            n = 2
        elif number % n == 0:
            result.append(n)
            number = number // n
        else:
            n += 1

    return result
