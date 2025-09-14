# Pythagix


Pythagix is a **high-performance, battle-tested Python library** for number theory and statistics. 
It delivers **blazing-fast, reliable, and precise implementations** of essential mathematical utilities, including prime checking, GCD/LCM, ratio simplification, triangular numbers, and more. 
Designed for developers, students, and researchers alike, Pythagix makes handling **massive numbers, complex computations, and advanced math operations** simple, efficient, and hassle-free.

Source code: https://github.com/UltraQuantumScriptor/pythagix


## Features

Primes & Factorization: is_prime, nth_prime, prime_factorization, prime_factors

GCD / LCM / Ratios: gcd, lcm, simplify_ratio, is_equivalent

Statistics: mean, median, mode, variance, pvariance, std_dev, pstd_dev

Other utilities: triangle_number, compress_0, product, nCr, get_factors

Each function is fully tested and designed for high performance with arbitrarily large integers.


## Installation

```bash
pip install pythagix
```


## Usage

```python
from pythagix import gcd, is_prime, nth_prime

# Compute GCD of large numbers
print(gcd([12345678901234567890, 98765432109876543210]))

# Check if a number is prime
print(is_prime(101))  # True

# Get the 1000th prime number
print(nth_prime(1000))
```


## Testing

Pythagix uses pytest for automated testing. To run the test suite:

```bash
pytest
```

All core functionality is verified for correctness and performance across large inputs.


## Contributing

Contributions are welcome. To report bugs, suggest improvements, or submit code enhancements:

### Open an issue on GitHub

Submit a pull request

Refer to the repository’s CONTRIBUTING.md for detailed guidelines.


## License

Pythagix is licensed under the MIT License.