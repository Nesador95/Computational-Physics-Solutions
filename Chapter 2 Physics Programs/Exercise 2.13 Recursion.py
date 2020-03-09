# Done
"""
In this file, we will rewrite previous programs and new programs using
recursive methods.
"""

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)

print(factorial(5))

def catalan_numbers(n):
    if n == 0:
        return 1
    else:
        return ( (4*n - 2) / (n + 1) ) * catalan_numbers(n - 1)

print(catalan_numbers(100))
        
def gratest_common_divisor(m,n):
    if n == 0:
        return m
    else:
        return gratest_common_divisor(n, m % n)   

print(gratest_common_divisor(108,192))

# Aside when there are programs that take a long time to work,
# it is useful to print an update while it works to make sure steps are being
# calculated for example on a recuring loop, one may add:

for n in range(1e7):
    if n % 1000 == 0:
        print("step", n)

