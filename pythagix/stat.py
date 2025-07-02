import math as m
from collections import Counter
from typing import Union
from functools import reduce
from .utils import middle

Numeric = Union[int, float]


def mean(values: list[Numeric]) -> float:
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


def median(values: list[Numeric]) -> float:
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


def mode(values: list[Numeric]) -> Union[Numeric, list[Numeric]]:
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


def variance(values: list[float]) -> float:
    """
    Work out the variance of the give list of numbers.

    Args:
        values (list[float]): a list of floats.

    Return:
        float: The variance of the list.
    """
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)


def std_dev(values: list[float]) -> float:
    """
    determine the standard deviation of the give list of numbers.

    Args:
        values (list[float]): a list of floats.

    Return:
        float: The standard deviation of the list.
    """
    return m.sqrt(variance(values))
