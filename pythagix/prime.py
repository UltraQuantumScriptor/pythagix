import math as m
from typing import List
from .numbering import count_factors


def is_prime(number: int) -> bool:
    """
    Check whether a given integer is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, m.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


def filter_primes(values: List[int]) -> List[int]:
    """
    Filter and return the prime numbers from a List.

    Args:
        values (List[int]): A List of integers.

    Returns:
        List[int]: A List containing only the prime numbers.
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

    count: int = 0
    candidate: int = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == position:
                return candidate
        candidate += 1


def prime_factors(number: int) -> List[int]:
    """
    Get all positive prime factors of the number.

    Args:
        number (int): an integer whose factors are to be found.

    Returns:
        int: The prime factors.

    Raises:
        ValueError: If the number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive")
    return sorted(
        set([factors for factors in count_factors(number) if is_prime(factors)])
    )
