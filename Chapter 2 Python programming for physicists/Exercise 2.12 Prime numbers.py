
# Done
import numpy as np

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

        