'''
15. Make a list of the largest or smallest N items in a collection.
'''
def find_largest(collection, N):
    return sorted(collection, reverse=True)[:N]

def find_smallest(collection, N):
    return sorted(collection)[:N]

# Get user input for the collection
collection_input = input("Enter a list of numbers separated by spaces: ")
collection = list(map(int, collection_input.split()))

# Get user input for N
N = int(input("Enter the value of N: "))

largest_items = find_largest(collection, N)
smallest_items = find_smallest(collection, N)

print(f"Largest {N} items:", largest_items)
print(f"Smallest {N} items:", smallest_items)
