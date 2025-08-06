import math as m
from functools import reduce
from typing import List, Sequence, Set, Union

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


def count_factors(number: int) -> int:
    """
    Returns the number of all positive divisors of the number.

    Args:
        number (int): the number whose divisors are to be counted.

    Returns:
        int: the number of divisors.
    """

    return len(get_factors(number))


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
