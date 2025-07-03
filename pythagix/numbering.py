import math as m
from functools import reduce
from typing import List, Set


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


def count_factors(number: int) -> List[int]:
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
