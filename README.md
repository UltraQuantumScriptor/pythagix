# 🧠 pythagix

Math utilities for number nerds.  
Check primes, compute triangle numbers, find GCDs — all in one lightweight package.  
Because math shouldn't be a pain 🧮✨

---

## 📦 Installation

```bash
pip install pythagix
```

⚙️ Features

🔢 is_prime(number) — Check if a number is prime

📜 prime_list([list]) — Return all primes in a list

🔎 nth_prime(n) — Get the n-th prime number

🤝 gcd([list]) — Greatest common divisor of a list

📏 is_perfect_square(n) — Check if n is a perfect square

🧱 count_factors(n) — Get all factors of a number

🔺 triangle_number(n) — Get the n-th triangle number

🧪 Examples
```python
from pythagix import is_prime, nth_prime, gcd, triangle_number

print(is_prime(13))        # True
print(nth_prime(10))       # 29
print(gcd([12, 18, 24]))   # 6
print(triangle_number(7))  # 28
```

📚 Why?
pythagix was built to give math students, coders, and tinkerers a fast and fun way to explore number theory in Python. No heavy dependencies. Just pure mathy goodness.