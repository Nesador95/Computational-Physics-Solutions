# Done
import numpy as np

###############################################################################
# Part a
###############################################################################

def standard_quadratic_equation_solver(a,b,c):
    
    x_plus = ( -b + np.sqrt(b**2 - 4*a*c) ) / (2*a)
    x_minus = ( -b - np.sqrt(b**2 - 4*a*c) ) / (2*a)
    return x_minus,x_plus

# compute the solution for 0.001x^2 + 1000x + 0.001 = 0


print(standard_quadratic_equation_solver(0.001,1000,0.001))

###############################################################################
# Part b
###############################################################################

def modified_quadratic_equation_solver(a,b,c):
    # this version multiplies ( -b +- np.sqrt(b**2 - 4*a*c) ) to top and bottom
    x_plus = (2*c) / ( -b - np.sqrt(b**2 - 4*a*c) )
    x_minus = (2*c) / ( -b + np.sqrt(b**2 - 4*a*c) )
    return x_minus,x_plus

print(modified_quadratic_equation_solver(0.001,1000,0.001))

###############################################################################
# Conclusion
###############################################################################

# The problem with both methods is that the computer only represents 10^16 
# digits of any number for operations; when you are substracting numbers, 
# the computer truncates any trailing digits after this limit and an accuracy
# that used to be of 10^16 could now be as low as two digits.
# by combining both methods, one can get more accurate answers.
# 
# This explanation is derived from the information given in pages 131-32 from 
# the book. 

def computational_quadratic_equation_solver(a,b,c):
    # this version minimazes the number of substractions.
    x_plus = ( -b + np.sqrt(b**2 - 4*a*c) ) / (2*a)
    x_minus = (2*c) / ( -b + np.sqrt(b**2 - 4*a*c) )
    return x_minus,x_plus

print(computational_quadratic_equation_solver(0.001,1000,0.001))