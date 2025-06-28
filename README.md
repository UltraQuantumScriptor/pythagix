# Pythagix

Pythagix is a lightweight, dependency-free Python library for number theory operations.
It provides a clean and efficient interface for common mathematical utilities such as prime checking, greatest common divisor, triangular numbers, and more.

---


Installation

You can install Pythagix using pip:

```bash
pip install pythagix
```


Features

count_factors(number: int) -> List[int]
Returns a sorted list of all positive factors of the given number.

digit_sum(number: int) -> int
Returns the sum of all digits in the given number.

filter_primes(values: List[int]) -> List[int]
Filters and returns prime numbers from a list of integers.

gcd(values: List[int]) -> int
Computes the greatest common divisor (GCD) of a list of integers.

is_perfect_square(number: int) -> bool
Determines whether a number is a perfect square.

is_prime(number: int) -> bool
Checks whether a number is prime.

is_multiple(number: int, base: int) -> bool
Checks if one number is a multiple of another.

lcm(values: List[int]) -> int
Computes the least common multiple (LCM) of a list of integers.

mean(values: List[int | float]) -> float
Calculates the arithmetic mean (average) of a list of numbers.

median(values: List[int | float]) -> float
Computes the median value of a list.

middle(a: int | float, b: int | float) -> float
Returns the midpoint of two numeric values.

mode(values: List[int | float]) -> int | float | List[int | float]
Computes the mode(s) of a list. Returns a single value or a list of modes.

nth_prime(position: int) -> int
Retrieves the n-th prime number (1-based index).

triangle_number(index: int) -> int
Computes the n-th triangular number.


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
