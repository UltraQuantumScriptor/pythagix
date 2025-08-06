import math as m
from collections import Counter
from typing import Union, List
from .utils import middle

Numeric = Union[int, float]


def mean(values: List[Numeric]) -> float:
    """
    Calculate the mean (average) of a List of numbers.

    Args:
        values (List[int, float]): A List of integers or floats.

    Returns:
        float: The mean of the List.

    Raises:
        ValueError: If the input List is empty.
    """
    if not values:
        raise ValueError("Must contain at least one data point")

    total: float = 0.0
    for number in values:
        total += number

    return total / len(values)


def median(values: List[Numeric]) -> float:
    """
    Calculate the median of a List of numbers.

    Args:
        values (List[Union[int float]]): A List of integers or floats.

    Returns:
        float: The median of the List.

    Raises:
        ValueError: If the input List is empty.
    """
    if not values:
        raise ValueError("Must contain at least one data point")

    values = sorted(values)
    length: int = len(values)
    mid: int = length // 2

    if length % 2 == 1:
        return float(values[mid])
    else:
        return middle(values[mid - 1], values[mid])


def mode(values: List[Numeric]) -> Union[Numeric, List[Numeric]]:
    """
    Compute the mode(s) of a List of numeric values.

    The mode is the number that appears most frequently in the List.
    If multiple numbers have the same highest frequency, all such numbers are returned as a List.
    If only one number has the highest frequency, that single value is returned.

    Args:
        values (List[Union[int, float]]): A List of integers or floats.

    Returns:
        Union[int, float, List[Union[int, float]]]:
            The mode of the List. Returns a single value if there's one mode,
            or a List of values if multiple modes exist.

    Raises:
        ValueError: If the input List is empty.
    """
    if not values:
        raise ValueError("Input List must not be empty")

    frequency = Counter(values)
    highest: Numeric = max(frequency.values())
    modes: List[Numeric] = [
        number for number, count in frequency.items() if count == highest
    ]

    return modes[0] if len(modes) == 1 else modes


def variance(values: List[Numeric]) -> float:
    """
    Work out the variance of the give List of numbers.

    Args:
        values (List[Union[int, float]]): a List of floats or integers.

    Return:
        float: The variance of the List.
    """
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)


def std_dev(values: List[Numeric]) -> float:
    """
    determine the standard deviation of the give List of numbers.

    Args:
        values (List[Union[int, float]]): a List of floats or integers.

    Return:
        float: The standard deviation of the List.
    """
    return m.sqrt(variance(values))
