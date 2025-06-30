import math as m
from functools import reduce


def gcd(values: list[int]) -> int:
    """
    Compute the greatest common divisor (GCD) of a list of integers.

    Args:
        values (List[int]): A list of integers.

    Returns:
        int: The GCD of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Input list must not be empty")
    return reduce(m.gcd, values)


def lcm(values: list[int]) -> int:
    """
    Compute the least common multiple (LCM) of a list of integers.

    Args:
        values (List[int]): A list of integers.

    Returns:
        int: The LCM of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Input list must not be empty")

    return reduce(m.lcm, values)


def count_factors(number: int) -> list[int]:
    """
    Return all positive factors of a number.

    Args:
        number (int): The number whose factors are to be found.

    Returns:
        List[int]: A sorted list of factors.

    Raises:
        ValueError: If the number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive")

    factors = set()
    for i in range(1, m.isqrt(number) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)
