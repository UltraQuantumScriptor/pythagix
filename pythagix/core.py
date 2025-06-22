def filter_prime(number_list: list[int]) -> list[int]:
    """
    Returns a list of all prime numbers from a given list.

    Args:
        number_list (list[int]): The list of integers to check.

    Returns:
        list[int]: A list containing only the prime numbers from the input.
    """
    prime_number: list[int] = []
    for x in number_list:
        if x == 1:
            continue
        for y in range(2, int(x * 1 / 2 + 1)):
            if x % y == 0:
                break
        else:
            prime_number.append(x)
    return prime_number


def is_prime(number: int) -> bool:
    """
    Checks whether a number is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for y in range(2, int(number * 1 / 2)):
        if number % y == 0:
            return False
    else:
        return True


def nth_prime(index: int) -> int:
    """
    Returns the n-th prime number (1-indexed).

    Args:
        index (int): The position of the prime to find.

    Returns:
        int: The n-th prime number.

    Raises:
        ValueError: If index is less than 1.
    """
    if index < 1:
        raise ValueError("Index must be >= 1")

    count: int = 0
    prime_number: int = 2
    while True:
        if is_prime(prime_number):
            count += 1
            if count == index:
                return prime_number
        prime_number += 1


def gcd(number_list: list[int]) -> int:
    """
    Returns the greatest common divisor (GCD) of a list of integers.

    Args:
        number_list (list[int]): The list of integers.

    Returns:
        int: The greatest number that divides all elements in the list.
    """
    num: int = 2
    highest: int = 0
    while num <= min(number_list):
        for number in number_list:
            if number % num != 0:
                break
        else:
            highest = num
        num += 1
    return highest


def is_perfect_square(number: int) -> bool:
    """
    Checks whether a number is a perfect square.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    num: int = 0
    while num <= number:
        if num**2 == number:
            return True
        num += 1
    return False


def count_factors(number: int) -> list[int]:
    """
    Returns a list of all factors (divisors) of a number.

    Args:
        number (int): The number to find factors of.

    Returns:
        list[int]: A list of all positive integers that divide the number evenly.
    """
    num: int = 1
    factors: list[int] = []
    while num <= number:
        if number % num == 0:
            factors.append(num)
        num += 1
    return factors


def triangle_number(number: int) -> int:
    """
    Returns the n-th triangle number.

    Args:
        number (int): The term (n) of the triangle number sequence.

    Returns:
        int: The n-th triangle number, calculated as n(n+1)//2.
    """
    return number * (number + 1) // 2


if __name__ == "__main__":

    def main():
        """Runs a quick test of any function."""
        print(triangle_number(10))

    main()
