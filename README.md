# Pythagix

Pythagix is a lightweight, dependency-free Python library for number theory operations.
It provides a clean and efficient interface for common mathematical utilities such as prime checking, greatest common divisor, triangular numbers, and more.

Installation
You can install Pythagix using pip:

```bash
pip install pythagix
```

Features

compress_0(values: int | float) -> list[int | float]
Clears consecutive zeros, keeping only one of the zero.

filter_primes(values: list[int]) -> list[int]
Filters and returns prime numbers from a list of integers.

gcd(values: list[int]) -> int
Computes the greatest common divisor (GCD) of a list of integers.

get_factors(number: int) -> List[int]
Return all positive factors of a number.

is_equivalent(ratio1: tuple[int, int], ratio2: tuple[int, int]) -> bool
Check if two ratios are equivalent by simplifying both and comparing.

is_prime(number: int) -> bool
Checks whether a number is prime.

lcm(values: list[int]) -> int
Computes the least common multiple (LCM) of a list of integers.

mean(values: list[int | float]) -> float
Calculates the arithmetic mean (average) of a list of numbers.

median(values: list[int | float]) -> float
Computes the median value of a list.

mode(values: list[int | float]) -> int | float | list[int | float]
Computes the mode(s) of a list. Returns a single value or a list of modes.

nCr(n: int, k: int) -> Union[int, float]
Count all possible k items from n.

nth_prime(position: int) -> int
Retrieves the n-th prime number (1-based index).

prime_factorization(number: int) -> Union[List[int], None]
Find all prime factors of the given number.

prime_factors(number: int) -> list[int]
Get all prime factors of the given number.

product(values: Sequence[int | float]) -> int | float
Multiplies the entire list until one number remains.

pstd_dev(values: Sequence[int | float]) -> float
Determine the standard deviation of the values (population).

pvariance(values: Sequence[int | float]) -> float
Work out the variance of the values (population).

simplify_ratio(ratio: tuple[int, int]) -> tuple[int, int]
Simplify a ratio by dividing both terms by their greatest common divisor (GCD).

std_dev(values: list[int | float]) -> float
Determine the standard deviation of the values (sample).

triangle_number(index: int) -> int
Computes the n-th triangular number.

variance(values: list[int | float]) -> float
Work out the variance of the values (sample).

Use Cases

Pythagix is suitable for:

Educational platforms and math-related applications

Prototyping number-theoretic algorithms

Teaching foundational concepts in discrete mathematics

Lightweight command-line tools and academic scripting

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute the software as permitted under the license terms.

Contributing

Contributions are welcome.

To report bugs, suggest enhancements, or submit code improvements, please open an issue or create a pull request via the GitHub repository.