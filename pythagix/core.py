import math as m
from functools import reduce
from typing import List, Tuple, Union
from collections import Counter

Numeric = Union[int, float]
Ratio = Tuple[int, int]

__all__ = [
    "count_factors",
    "digit_sum",
    "filter_primes",
    "from_percentage",
    "gcd",
    "is_equivalent",
    "is_perfect_square",
    "is_prime",
    "is_multiple",
    "lcm",
    "mean",
    "median",
    "middle",
    "mode",
    "nth_prime",
    "simplify_ratio",
    "to_percentage",
    "triangle_number",
]


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
    return reduce(m.gcd, values)


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


def count_factors(number: int) -> List[int]:
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


def triangle_number(index: int) -> int:
    """
    Calculate the N-th triangular number.

    Args:
        index (int): The position (starting from 0) in the triangular number sequence.

    Returns:
        int: The N-th triangular number.

    Raises:
        ValueError: If the index is negative.
    """
    if index < 0:
        raise ValueError("Index must be >= 0")
    return index * (index + 1) // 2


def lcm(values: List[int]) -> int:
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
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        float: The average of the two numbers.
    """
    return (a + b) / 2


def mean(values: List[Numeric]) -> float:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        values (List[int | float]): A list of integers or floats.

    Returns:
        float: The mean of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("Must contain at least one data point")

    total = 0
    for number in values:
        total += number

    return total / len(values)


def median(values: List[Numeric]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        values (List[int | float]): A list of integers or floats.

    Returns:
        float: The median of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("Must contain at least one data point")

    values = sorted(values)
    length = len(values)
    mid = length // 2

    if length % 2 == 1:
        return float(values[mid])
    else:
        return middle(values[mid - 1], values[mid])


def mode(values: List[Numeric]) -> Union[Numeric, List[Numeric]]:
    """
    Compute the mode(s) of a list of numeric values.

    The mode is the number that appears most frequently in the list.
    If multiple numbers have the same highest frequency, all such numbers are returned as a list.
    If only one number has the highest frequency, that single value is returned.

    Args:
        values (List[int | float]): A list of integers or floats.

    Returns:
        int | float | List[int | float]:
            The mode of the list. Returns a single value if there's one mode,
            or a list of values if multiple modes exist.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("Input list must not be empty")

    frequency = Counter(values)
    highest = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == highest]

    return modes[0] if len(modes) == 1 else modes


def from_percentage(percentage: Numeric) -> float:
    """
    Convert the percentage to a decimal.

    Args:
        percentage (int | float): The percentage which is to be converted
        to decimal.

    Returns:
        float: The decimal calculated from percentage.
    """
    return percentage / 100


def to_percentage(number: Numeric) -> Numeric:
    """
    Convert a decimal to a percentage.

    Args:
        number (int | float): The part or value to convert into a percentage.
        total (int | float): The total or whole against which the percentage is calculated.

    Returns:
        float: The percentage of number relative to total.
    """
    return number * 100


def simplify_ratio(ratio: Ratio) -> Ratio:
    """
    Simplify a ratio by dividing both terms by their greatest common divisor (GCD).

    Args:
        ratio (tuple[int, int]): A ratio represented as a tuple (a, b).

    Returns:
        tuple[int, int]: The simplified ratio with both values reduced.
    """
    a, b = ratio
    g = m.gcd(a, b)
    return (a // g, b // g)


def is_equivalent(ratio1: Ratio, ratio2: Ratio) -> bool:
    """
    Check if two ratios are equivalent by simplifying both and comparing.

    Args:
        ratio1 (tuple[int, int]): The first ratio to compare.
        ratio2 (tuple[int, int]): The second ratio to compare.

    Returns:
        bool: True if both ratios are equivalent, False otherwise.
    """
    return simplify_ratio(ratio1) == simplify_ratio(ratio2)


if __name__ == "__main__":

    def main() -> None:
        """Tester Function."""
        print(is_equivalent((2, 4), (1, 2)))

    main()
