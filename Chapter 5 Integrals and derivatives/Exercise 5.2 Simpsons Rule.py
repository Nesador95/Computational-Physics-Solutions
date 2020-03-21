#Not Done
import numpy as np
import matplotlib.pyplot as plt
import Integration_Methods as IM 

class SimpsonsRuleIntegration:

    def function_integration(self, start, stop, num_slices):

        bound_a = start
        bound_b = stop
    
        width = (bound_b - bound_a) / num_slices
        summation =  (f(bound_a) + f(bound_b))
        summation_even = 0
        summation_odd = 0

        for odd in range(1, num_slices, 2):
            summation_odd += (f(bound_a + (odd*width)))
        summation_odd *=  4

        for even in range(2, num_slices, 2):
            summation_even += (f(bound_a + (even*width)))
        summation_even *= 2
        
    
        summation += summation_odd + summation_even
        summation *= (1/3) * width
        return summation

        def data_integration(self, data):

            bound_a = data[0]
            bound_b = data[-1]
    
            width = (bound_b - bound_a) / len(data)
            summation =  (bound_a + bound_b)
            summation_even = 0
            summation_odd = 0
            for odd in range(1, len(data), 2):
                summation_odd += data[odd]
            summation_odd *= 4

            for even in range(2, len(data), 2):
                summation_even += data[even]
            summation_even *= 2

    
            summation += summation_odd + summation_even
            summation *= (1/3) * width
            return summation

###############################################################################
# Part a & b & c
###############################################################################

def f(x):
    return x**4 - 2*x +1

solution = SimpsonsRuleIntegration().function_integration(0,2,10)
print(solution, 4/solution)




equation = IM.equation("x**4 - 2*x +1" , ["x"])
Trapesoid_comparison = IM.TrapesiumRuleIntegration().function_integration(equation,0,2,10)

print("The Trapezoidal Rule returned this: " + str(Trapesoid_comparison)\
     + " Simpson's Rule returned this: " + str(solution) + " both with 10 slices each"\
      + " Their accuracy to the actual answer of 4.4 is " + str(4/Trapesoid_comparison) +" and " \
      +  str(4/solution) + " for trapezoidal and Simpson's respectively.")