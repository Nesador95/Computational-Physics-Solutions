# Done
import numpy as np 

def f(x):
    f = x*(x - 1)
    return f


def derivative(value, delta):
    x = value
    d = delta
    return ( f(x + d) - f(x) ) / d

print(derivative( 1, 1e-2))
print(derivative( 1, 1e-4))
print(derivative( 1, 1e-6))
print(derivative( 1, 1e-8))
print(derivative( 1, 1e-10))
print(derivative( 1, 1e-12))
print(derivative( 1, 1e-14))

###############################################################################
# Conclusion
###############################################################################

# I believe that the calculations first get better and then get worse for the
# same reason as in exercise 4.2 substracting really small digits between floats
# is the worse case scenario for accuracy. Although addition is not perfect,
# substraction can really affect accuracy the bigger the differece between digits
# is and how samall the substraction difference is.
 