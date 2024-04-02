"""
        1. Write a prime generator program using only primes and using python loops.
"""


def is_prime(num, div=2):
    """
    Check if a number is prime recursively.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % div == 0:
        return False
    if div * div > num:
        return True
    return is_prime(num, div + 1)

def prime_generator(start=2):
    """
    Generate prime numbers using a generator recursively.
    """
    if is_prime(start):
        yield start
    yield from prime_generator(start + 1)

# Example usage:
generator = prime_generator()
for _ in range(10):
    print(next(generator))
