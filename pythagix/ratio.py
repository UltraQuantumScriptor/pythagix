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

    Raises:
        ZeroDivisionError: if the denominator is 0
    """
    a, b = ratio
    if b == 0:
        raise ZeroDivisionError("Denominator must not be zero")
    if a == 0:
        return (0, 1)

    g = m.gcd(a, b)
    a, b = a // g, b // g

    if b < 0:
        a, b = -a, -b

    return (a, b)


def is_equivalent(*ratio: Ratio) -> bool:
    """
    Check if all provided ratios are equivalent.

    Each ratio is simplified before comparison, so (2, 4) and (1, 2) are considered equal.

    Args:
        *ratios (Ratio): One or more ratios to compare, each as a tuple (numerator, denominator).

    Returns:
        bool: True if all ratios are equivalent, False otherwise.
    """

    if not ratio:
        return True

    base = simplify_ratio(ratio[0])
    for r in ratio[1:]:
        if simplify_ratio(r) != base:
            return False
    return True
