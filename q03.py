"""
    3. Print first 10 odd and even numbers using iterators and compress. You can use duck typing.
"""
from itertools import compress

def odd_numbers():
    current = 1
    while True:
        yield current
        current += 2

def even_numbers():
    current = 0
    while True:
        yield current
        current += 2

odd_iterator = odd_numbers()
even_iterator = even_numbers()

first_10_odd = list(compress(odd_iterator, [True]*10))
first_10_even = list(compress(even_iterator, [True]*10))

print("First 10 odd numbers:", first_10_odd)
print("First 10 even numbers:", first_10_even)
