# Done 

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)

###############################################################################
# Test with integers
###############################################################################

print(factorial(200))

###############################################################################
# Test with integers
###############################################################################

print(factorial(200.0))

###############################################################################
# Conclusion 
###############################################################################

# Integers can be calculated to arbitrarely long digits were as Python has a
# hard limit for float numbers; This limit is 1.79769x10^308 anything larger
# and it prints inf for infinity. This also applies to the smallest float 
# number: 2.22507x10^-308 that defaults to 0 if exceeded.