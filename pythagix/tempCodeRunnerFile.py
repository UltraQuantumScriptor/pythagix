# Only call is_prime for harder checks
        if is_prime(candidate):
            count += 1
            if count == position:
                return candidate