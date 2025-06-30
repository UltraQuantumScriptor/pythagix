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
