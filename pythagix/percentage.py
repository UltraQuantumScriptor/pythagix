from typing import Union

Numeric = Union[int, float]


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

    Returns:
        float: The percentage of number relative to total.
    """
    return number * 100


def percentage_of(number: Numeric, percentage: Numeric) -> float:
    """
    Calculate the given percentage of a value.

    Parameters:
        value (float or int): The total number you want a percentage of.
        percent (float or int): The percentage to calculate.

    Returns:
        float: The result of (percent / 100) * value.
    """
    return (number * percentage) / 100
