from functools import lru_cache
import random
from typing import List


@lru_cache(maxsize=None)
def is_prime(n: int, k: int = 12) -> bool:
    """
    Check whether a given integer is a prime number.

    Args:
        n (int): The number to check.
        k (int): The number of rounds to check if the number is prime or not.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def filter_primes(values: List[int]) -> List[int]:
    """
    Filter a list of numbers, returning only the primes.

    Args:
        nums (list[int]): List of numbers to filter.

    Returns:
        list[int]: List of primes.
    """
    return [n for n in values if is_prime(n)]


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
    if position == 1:
        return 2

    count = 1
    candidate = 3

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    while True:
        if any(candidate % p == 0 for p in small_primes if p < candidate):
            candidate += 2
            continue

        if is_prime(candidate):
            count += 1
            if count == position:
                return candidate
        candidate += 2
