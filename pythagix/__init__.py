from .numbering import compress_0, get_factors, nCr
from .prime import filter_primes
from .ratio import simplify_ratio, is_equivalent
from .stat import product

from .fraction import UnitFraction, SmartFraction
from .pprime import is_prime, nth_prime
from .figurates import triangle_number
from .pnumbering import gcd, lcm
from .pstat import mean, median, mode, std_dev, variance, pstd_dev, pvariance

__all__ = (
    # Fraction
    "UnitFraction",
    "SmartFraction",
    # Numbers
    "gcd",
    "get_factors",
    "lcm",
    "compress_0",
    "nCr",
    # Primes
    "is_prime",
    "nth_prime",
    "filter_primes",
    # Figurates
    "triangle_number",
    # Ratios
    "simplify_ratio",
    "is_equivalent",
    # Statistics
    "mean",
    "median",
    "mode",
    "std_dev",
    "variance",
    "pvariance",
    "pstd_dev",
    "product",
)
