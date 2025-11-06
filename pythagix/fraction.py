import math as m
from fractions import Fraction


class UnitFraction:
    """
    A class that represents a fraction with an associated unit (symbol).

    Args:
        fraction (tuple[int, int]): The numerator and denominator of the fraction.
        symbol (str): The unit of the fraction (e.g., "m", "s").

    Functionality:
        Addition/Subtraction:
            Addition/Subtraction between two fractions can ONLY be performed if they have the same unit.
        Multiplication:
            Multiplying two fractions results in the concatenation of the two symbols as they are.
        Dividing:
            Dividing two fractions results in the concathenation of two symbols and puts a '/' in between them.


    Raises:
        TypeError:
            If addition or subtraction is attempted between fractions with different units.
            If an unsupported operation is attempted with a non-compatible type.
    """

    def __init__(self, fraction: tuple[int, int], symbol: str) -> None:
        self.fraction = fraction
        self.symbol = symbol
        if fraction[1] == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

    def simplify(self) -> "UnitFraction":
        numerator, denominator = self.fraction
        gcd = m.gcd(numerator, denominator)
        return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

    def to_float(self) -> float:
        numerator, denominator = self.fraction
        return numerator / denominator

    def __add__(self, other) -> "UnitFraction":
        if isinstance(other, int):
            numerator = self.fraction[0] + other * self.fraction[1]
            denominator = self.fraction[1]
            gcd = m.gcd(numerator, denominator)
            return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

        if isinstance(other, UnitFraction):
            if self.symbol == other.symbol:
                a, b = self.fraction
                c, d = other.fraction
                numerator = a * d + c * d
                denominator = b * d
                gcd = m.gcd(numerator, denominator)
                return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)
            else:
                raise TypeError(
                    f"Cannot add fractions with units '{self.symbol}' and '{other.symbol}'"
                )

        elif isinstance(other, float):
            fraction = Fraction(f"{other}")
            a, b = self.fraction
            c, d = fraction.numerator, fraction.denominator
            numerator = a * d + c * b
            denominator = b * d
            gcd = m.gcd(numerator, denominator)
            return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

        else:
            raise TypeError(
                f"Unsupported operand type(s) for '+': UnitFraction and {type(other).__name__}"
            )

    def __sub__(self, other) -> "UnitFraction":
        if isinstance(other, int):
            numerator = self.fraction[0] - other * self.fraction[1]
            denominator = self.fraction[1]
            gcd = m.gcd(numerator, denominator)
            return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

        if isinstance(other, UnitFraction):
            if self.symbol == other.symbol:
                a, b = self.fraction
                c, d = other.fraction
                numerator = a * d - c * d
                denominator = b * d
                gcd = m.gcd(numerator, denominator)
                return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)
            else:
                raise TypeError(
                    f"Cannot subtract fractions with units '{self.symbol}' and '{other.symbol}'"
                )

        elif isinstance(other, float):
            fraction = Fraction(f"{other}")
            a, b = self.fraction
            c, d = fraction.numerator, fraction.denominator
            numerator = a * d - c * d
            denominator = b * d
            gcd = m.gcd(numerator, denominator)
            return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

        else:
            raise TypeError(
                f"Unsupported operand type(s) for '-': UnitFraction and {type(other).__name__}"
            )

    def __mul__(self, other) -> "UnitFraction":
        if isinstance(other, int):
            numerator = self.fraction[0] * other
            denominator = self.fraction[1]
            symbol = self.symbol

        elif isinstance(other, float):
            fraction = Fraction(f"{other}")
            numerator = self.fraction[0] * fraction.numerator
            denominator = self.fraction[1] * fraction.denominator
            symbol = self.symbol
        elif isinstance(other, UnitFraction):

            a, b = self.fraction
            c, d = other.fraction
            numerator = a * c
            denominator = b * d
            symbol = f"{self.symbol+other.symbol}"

        else:
            raise TypeError(
                f"Unsupported operand type(s) for '*': UnitFraction and {type(other).__name__}"
            )

        gcd = m.gcd(numerator, denominator)
        return UnitFraction((numerator // gcd, denominator // gcd), symbol)

    def __truediv__(self, other) -> "UnitFraction":
        if isinstance(other, int):
            numerator = self.fraction[0]
            denominator = self.fraction[1] * other
            symbol = self.symbol

        elif isinstance(other, float):
            fraction = Fraction(f"{other}")
            numerator = self.fraction[0] * fraction.denominator
            denominator = self.fraction[1] * fraction.numerator
            symbol = self.symbol

        elif isinstance(other, UnitFraction):
            a, b = self.fraction
            c, d = other.fraction
            numerator = a * d
            denominator = c * b
            symbol = f"{self.symbol}/{other.symbol}"

        else:
            raise TypeError(
                f"Unsupported operand type(s) for '/': UnitFraction and {type(other).__name__}"
            )

        gcd = m.gcd(numerator, denominator)
        return UnitFraction((numerator // gcd, denominator // gcd), symbol)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        neg_self = UnitFraction((-self.fraction[0], self.fraction[1]), self.symbol)
        return neg_self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        a, b = self.fraction
        reciprocal = UnitFraction((b, a), f"1/{self.symbol}")
        return reciprocal.__mul__(other)

    def __neg__(self) -> "UnitFraction":
        numerator, denominator = self.fraction
        return UnitFraction((-numerator, denominator), self.symbol)

    def __eq__(self, other) -> bool:
        n1, d1 = self.fraction
        gcd = m.gcd(n1, d1)
        n1, d1 = n1 // gcd, d1 // gcd
        if isinstance(other, UnitFraction):
            n2, d2 = other.fraction
            gcd2 = m.gcd(n2, d2)
            n2, d2 = n2 // gcd2, d2 // gcd2
            if n1 == n2 and d1 == d2:
                return True
            return False
        elif isinstance(other, (int, float)):
            return n1 / d1 == other
        return False

    def __lt__(self, other) -> bool:  # <
        if isinstance(other, UnitFraction):
            if self.symbol != other.symbol:
                raise TypeError(
                    f"Cannot compare units '{self.symbol}' and '{other.symbol}'"
                )
            a, b = self.fraction
            c, d = other.fraction
            return a / b < c / d
        elif isinstance(other, (int, float)):
            a, b = self.fraction
            return a / b < other
        else:
            return NotImplemented

    def __le__(self, other) -> bool:  # <=
        if isinstance(other, UnitFraction):
            if self.symbol != other.symbol:
                raise TypeError(
                    f"Cannot compare units '{self.symbol}' and '{other.symbol}'"
                )
            a, b = self.fraction
            c, d = other.fraction
            return a / b <= c / d
        elif isinstance(other, (int, float)):
            a, b = self.fraction
            return a / b <= other
        else:
            return NotImplemented

    def __gt__(self, other) -> bool:  # >
        if isinstance(other, UnitFraction):
            if self.symbol != other.symbol:
                raise TypeError(
                    f"Cannot compare units '{self.symbol}' and '{other.symbol}'"
                )
            a, b = self.fraction
            c, d = other.fraction
            return a / b > c / d
        elif isinstance(other, (int, float)):
            a, b = self.fraction
            return a / b > other
        else:
            return NotImplemented

    def __ge__(self, other) -> bool:  # >=
        if isinstance(other, UnitFraction):
            if self.symbol != other.symbol:
                raise TypeError(
                    f"Cannot compare units '{self.symbol}' and '{other.symbol}'"
                )
            a, b = self.fraction
            c, d = other.fraction
            return a / b >= c / d
        elif isinstance(other, (int, float)):
            a, b = self.fraction
            return a / b >= other
        else:
            return NotImplemented

    def __abs__(self) -> "UnitFraction":
        numerator, denominator = self.fraction
        numerator, denominator = abs(numerator), abs(denominator)
        return UnitFraction((numerator, denominator), self.symbol)

    def __repr__(self) -> str:
        return f"{self.fraction[0]}/{self.fraction[1]} {self.symbol}"
