---

# Pythagix

Pythagix is a lightweight and dependency-free Python library designed for number theory operations.
It provides a clean, efficient interface to common mathematical utilities such as prime number checks, greatest common divisor computation, triangular numbers, and more.

---

## Installation

Install Pythagix using pip:

```bash
pip install pythagix
```

---

## Features

count_factors(number: int) -> List[int]
Return a sorted list of all positive factors of the given number.

digit_sum(number: int) -> int
Return the sum of all digit in the given number.

filter_primes(numbers: List[int]) -> List[int]
Return all prime numbers from a list of integers.

gcd(values: List[int]) -> int
Compute the greatest common divisor (GCD) of a list of integers.

is_perfect_square(number: int) -> bool
Check whether a number is a perfect square.

is_prime(number: int) -> bool
Determine whether a number is prime.

lcm(values: List[int]) -> int
Compute the least common multiple (LCM) of a list of integers.

middle(a: int | float, b: int | float) -> float
Return the midpoint of two numbers.

nth_prime(position: int) -> int
Retrieve the n-th prime number (1-based index).

triangle_number(index: int) -> int
Compute the n-th triangular number.

---

## Example Usage

```python
from pythagix import is_prime, nth_prime, gcd, triangle_number

print(is_prime(13))         # Output: True

print(nth_prime(10))        # Output: 29

print(gcd([12, 18, 24]))    # Output: 6

print(triangle_number(7))   # Output: 28
```

---

## Use Cases

Pythagix is ideal for:

Educational platforms and math-related tools

Prototyping algorithms and number-theoretic computations

Teaching foundational concepts in discrete mathematics and number theory

Lightweight CLI utilities and academic scripting

---

## License

Pythagix is released under the [MIT License](LICENSE), making it free to use, modify, and distribute.

---

## Contributing

Contributions are welcome!
If you'd like to add features, report bugs, or improve documentation, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/pythagix).

---

If you want me to tailor this even more (e.g. add badges, GitHub Actions, versioning, or PyPI metadata snippets), I can assist with that too.
