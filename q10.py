'''
10.
Write a code which yields all terms of the geometric progression a, aq, aq 2 , aq 3 , ....
When the progression produces a term that is greater than 100,000, the generator stops (with
a return statement). Compute total time and time within the loop.

'''

import time

def geometric_progression(a, q):
    start_time = time.time()  # Start time
    
    term = a
    while term <= 100000:
        yield term
        term *= q
    
    end_time = time.time()  # End time
    total_time = end_time - start_time
    print("Total time:", total_time)

# Example usage:
a = 2
q = 3
generator = geometric_progression(a, q)

start_loop_time = time.time()  # Start loop time
for term in generator:
    print(term)
end_loop_time = time.time()  # End loop time
loop_time = end_loop_time - start_loop_time
print("Time within loop:", loop_time)
