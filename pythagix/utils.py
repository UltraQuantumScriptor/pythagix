import math as m
from typing import Union

Numeric = Union[int, float]


def is_perfect_square(number: int) -> bool:
    """
    Check whether a number is a perfect square.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    if number < 0:
        return False
    root = m.isqrt(number)
    return root * root == number


def digit_sum(number: int) -> int:
    """
    Sum all digits of the given number.

    Args:
        number (int): The number whose digits are to be summed.

    Returns:
        int: The sum of the digits in the number.
    """
    return sum(int(digit) for digit in str(number))


def is_multiple(number: int, base: int) -> bool:
    """
    Check if a number is a multiple of another number.

    Args:
        number (int): The number to test.
        base (int): The base to check against.

    Returns:
        bool: True if number is a multiple of base, False otherwise.
    """
    return number % base == 0


def middle(a: Numeric, b: Numeric) -> float:
    """
    Return the midpoint between two numbers.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.

    Returns:
        float: The average of the two numbers.
    """
    return (a + b) / 2
