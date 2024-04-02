"""  
9. Enumerate the sequence of all lowercase ASCII letters, starting from 1, using
enumerate.
"""

lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

for index, letter in enumerate(lowercase_letters, start=1):
    print(index, letter)
