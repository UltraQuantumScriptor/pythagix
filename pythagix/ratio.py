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

    if b == 0:
        raise ZeroDivisionError("Denominator must not be a zero")
    if a == 0:
        return (0, 1)

    g: int = m.gcd(a, b)
    a, b = a // g, b // g

    if b < 0:
        a, b = -a, -b

    return (a, b)


def is_equivalent(*ratio: Ratio) -> bool:
    """
    Check if two ratios are equivalent by simplifying both and comparing.

    Args:
        ratio1 (Tuple[int, int]): The first ratio to compare.
        ratio2 (Tuple[int, int]): The second ratio to compare.

    Returns:
        bool: True if both ratios are equivalent, False otherwise.
    """

    def normalize(ratio: Ratio) -> Ratio:
        a, b = ratio

        if b == 0:
            raise ZeroDivisionError("Denominator must not be a zero")
        if a == 0:
            return (0, 1)

        g: int = m.gcd(a, b)
        a, b = a // g, b // g

        if b < 0:
            a, b = -a, -b

        return (a, b)

    base = normalize(ratio[0])
    for r in ratio[1:]:
        if normalize(r) != base:
            return False
    return True
