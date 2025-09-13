import math as m
from functools import lru_cache, reduce
import random
from typing import List, Sequence, Union
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
