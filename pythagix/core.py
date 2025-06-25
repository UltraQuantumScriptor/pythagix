from math import isqrt
from functools import reduce
from typing import List
import math

__all__ = [
    "is_prime",
    "filter_primes",
    "nth_prime",
    "gcd",
    "is_perfect_square",
    "count_factors",
    "triangle_number",
]


def is_prime(number: int) -> bool:
    """
    Check whether a given integer is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


def filter_primes(values: List[int]) -> List[int]:
    """
    Filter and return the prime numbers from a list.

    Args:
        values (List[int]): A list of integers.

    Returns:
        List[int]: A list containing only the prime numbers.
    """
    return [num for num in values if is_prime(num)]


def nth_prime(position: int) -> int:
    """
    Get the N-th prime number (1-based index).

    Args:
        position (int): The index (1-based) of the prime number to find.

    Returns:
        int: The N-th prime number.

    Raises:
        ValueError: If position < 1.
    """
    if position < 1:
        raise ValueError("Position must be >= 1")

    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == position:
                return candidate
        candidate += 1


def gcd(values: List[int]) -> int:
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
    return reduce(math.gcd, values)


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
    root = isqrt(number)
    return root * root == number


def count_factors(number: int) -> List[int]:
    """
    Return all positive factors of a number.

    Args:
        number (int): The number whose factors are to be found.

    Returns:
        List[int]: A sorted list of factors.

    Raises:
        ValueError: If number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive")

    factors = set()
    for i in range(1, isqrt(number) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)


def triangle_number(index: int) -> int:
    """
    Calculate the N-th triangular number.

    Args:
        index (int): The position (starting from 0) in the triangular number sequence.

    Returns:
        int: The N-th triangular number.

    Raises:
        ValueError: If index is negative.
    """
    if index < 0:
        raise ValueError("Index must be >= 0")
    return index * (index + 1) // 2


def main() -> None:
    """Tester Function."""
    ...


if __name__ == "__main__":
    main()
