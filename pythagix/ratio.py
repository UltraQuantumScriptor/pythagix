import math as m
from typing import Tuple

Ratio = Tuple[int, int]


def simplify_ratio(ratio: Ratio) -> Ratio:
    """
    Simplify a ratio by dividing both terms by their greatest common divisor (GCD).

    Args:
        ratio (Tuple[int, int]): A ratio represented as a Tuple (a, b).

    Returns:
        Tuple[int, int]: The simplified ratio with both values reduced.
    """
    a, b = ratio
    g: int = m.gcd(a, b)
    return (a // g, b // g)


def is_equivalent(ratio1: Ratio, ratio2: Ratio) -> bool:
    """
    Check if two ratios are equivalent by simplifying both and comparing.

    Args:
        ratio1 (Tuple[int, int]): The first ratio to compare.
        ratio2 (Tuple[int, int]): The second ratio to compare.

    Returns:
        bool: True if both ratios are equivalent, False otherwise.
    """
    return simplify_ratio(ratio1) == simplify_ratio(ratio2)
