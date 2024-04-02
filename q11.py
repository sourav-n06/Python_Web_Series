'''
11.
Search for palindrome and unique words in a text using string method.
'''
def find_palindromes(text):
    words = text.lower().split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes

def find_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return unique_words

# Example usage:
text = "Able was I ere I saw Elba"
palindromes = find_palindromes(text)
print("Palindromes:", palindromes)

unique_words = find_unique_words(text)
print("Unique words:", unique_words)
