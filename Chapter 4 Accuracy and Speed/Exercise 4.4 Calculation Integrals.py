# Not Done
import numpy as np
import time


def f(x):
    return np.sqrt(1-x**2)

def integral_slice_method(number_of_slices):
    h = 2/number_of_slices
    total = 0.0
    for k in range(number_of_slices):
        x_k = -1+h*k
        total += h*f(x_k)
    return total

start = time.time()
print(integral_slice_method(100))
end = time.time()
print(end-start)

start = time.time()
print(integral_slice_method(500000))
end = time.time()
print(end-start)
###############################################################################
# Conclusion
###############################################################################

# for this program to run for roughly about 1 second, we can get up to 9 digits 
# of accuracy in our calculations for the integral of this function.