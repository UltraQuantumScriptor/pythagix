import fractions
import math as m


class UnitFraction:
    def __init__(self, fraction: tuple[int, int], symbol: str) -> None:
        self.fraction = fraction
        self.symbol = symbol

    def __radd__(self, other):
        return self + other

    def __add__(self, other) -> object:
        if isinstance(other, int):
            numerator = self.fraction[0] + other * self.fraction[1]
            denominator = self.fraction[1]
            gcd = m.gcd(numerator, denominator)
            return UnitFraction((numerator // gcd, denominator // gcd), self.symbol)

        if isinstance(other, UnitFraction):
            if self.symbol == other.symbol:

                a, b = self.fraction
                c, d = other.fraction

                numerator = a * d + b * c
                denominator = b * d

                gcd = m.gcd(numerator, denominator)
                numerator //= gcd
                denominator //= gcd
                total = (numerator, denominator)
                return UnitFraction(total, self.symbol)
            else:

                raise TypeError(
                    f"Cannot add two fraction with units '{self.symbol}' and '{other.symbol}'"
                )
        else:

            raise TypeError(
                f"Unsupported operand type(s) for '+': UnitFraction and {type(other).__name__} "
            )

    def __repr__(self) -> str:
        return f"{self.fraction[0]}/{self.fraction[1]}"


class SmartFraction:
    def __init__(self, fraction: tuple[int, int], uncertainty: float) -> None:
        self.fraction = fraction
        self.uncertainty = uncertainty

    def frac_range(self) -> tuple[float, float]:
        low = self.fraction[0] / self.fraction[1] - self.uncertainty
        high = self.fraction[0] / self.fraction[1] + self.uncertainty
        return (low, high)

    def __repr__(self) -> str:
        return f"{self.fraction}"
