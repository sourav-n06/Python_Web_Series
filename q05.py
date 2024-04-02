"""
5. Write first seven Fibinacci numbers using generator next function/ yield in python. Trace
and memorize the function. Also check whether a user given number is Fibinacci or not.
    """
    
def fibonacci_generator():
    a, b = 0, 1
    yield a
    yield b
    for _ in range(5):
        a, b = b, a + b
        yield b

def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

fib_numbers = list(fibonacci_generator())
print("First seven Fibonacci numbers:", fib_numbers)

user_input = int(input("Enter a number to check if it's Fibonacci: "))
if user_input in fib_numbers:
    print(f"{user_input} is a Fibonacci number.")
else:
    print(f"{user_input} is not a Fibonacci number.")
