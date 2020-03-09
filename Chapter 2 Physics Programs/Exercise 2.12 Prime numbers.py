
# Done
import numpy as np
"""
We are going to develop a program that finds prime numbers that is more efficient

A) a number is prime if it has no prime factors less than n. Hense we only need to
check if it is divisible by other primes. (ONLY NEED TO DIVIDE BY PRIMES)

B) If a number n is non-prime, having a factor r, then n=rs, where s is also a factor.
If r >= sqrt(n) then n = rs >= sqrt(n)s, which implies that s <= sqrt(n). In other words,
any non-prime must have factors, and hence also prime factors, less than or qual to sqrt(n).
Thus to determine if a number is prime we have to check its prime factors only up to and 
including sqrt(n) if there are none then the number is prime. (DIVIDE BY PRIMES UP TO sqrt(n))

C) If we find even a single prime factor less than sqrt(n) the we know that the number is 
non-prime, and hence there is no need to check any further - we can abandon this number and
move on to something else. 

"""


def prime_number_calculator(limit):

    list_of_primes = [2]
    number = 3
    while number <= limit:
        for prime in list_of_primes:
            if number % prime == 0:
                break
            elif prime > np.sqrt(number):
                list_of_primes.append(number)
                break
        number +=1
    return list_of_primes

print(prime_number_calculator(10000))

        