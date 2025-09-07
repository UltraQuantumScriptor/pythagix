from functools import lru_cache
import math as m
import random
from typing import List


@lru_cache(maxsize=None)
def is_prime(n: int, k=12) -> bool:
    """
    Check whether a given integer is a prime number.

    Args:
        n (int): The number to check.
        k (int): The number of rounds to check if the number is prime or not.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


@lru_cache(maxsize=None)
def filter_primes(values: List[int], reverse: bool = False) -> List[int]:
    """
    Filter and return the prime numbers from a List.

    Args:
        values (List[int]): A List of integers.
        reverse (bool = False): Sorts the list in descending order.
            default as False

    Returns:
        List[int]: A List containing only the prime numbers.
    """
    result = [num for num in values if is_prime(num)]

    if not reverse:
        return result
    return result[::-1]


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
