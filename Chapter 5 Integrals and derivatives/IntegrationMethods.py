import numpy as np
from Equation import Expression

def equation(equation, variables):
    """
    Note: This requires that you install the package Equation:
    https://pypi.org/project/Equation/#description

    Write your equation to be integrated here in the following format:
    ("equation" , ["variable"])

    example:
    equation = equation("x**4 - 2*x +1" , ["x"])
    
    Note: 
    - Does not interprete np.exp, write instead e
    - Does not interprete 4**(-2), write instead 1/4**2
    """
    f = Expression(equation, variables)
    return f

class TrapeziumRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using the trapezium/trapezoidal integration method.  
    """

    def function_integration(self,equation, bound_a, bound_b, num_slices):
        """    
        To use this method, define the equation first with
        the method equation, then pass the equation to this method,
        provide the bounderies and the number of slices 
        for the trapezoidal rule to execute.

        example:
        function_integration(equation, 0, 2, 10)
        """
        f = equation
        width = (bound_b - bound_a) / num_slices
        summation = 0.5*(f(bound_a) + f(bound_b))
        for portion in range(1, num_slices):
            summation += f(bound_a + portion * width)
        summation *= width
        return summation
        
    
    def data_integration(self, data):
        """
        To use the data_integration method, one must provide the data in an array form.
        """
        N_slices = len(data)
        width = (data[-1] - data[0]) / N_slices
        summation = 0.5*(data[0] + data[-1])
        for datum in range(N_slices):
            summation += (data[datum])
        summation *= width
        return summation

class SimpsonsRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using Simpson's Rule integration method. note that Simpson's Rule requires
    an even number of steps to work properly.

    
    """
    def function_integration(self,equation, bound_a, bound_b, num_slices):
        """    
        To use this method, define the equation first with
        the method equation, then pass the equation to this method,
        provide the bounderies and the number of slices 
        for Simpson's rule to execute.

        example:
        function_integration(equation, 0, 2, 10)
        """ 
        f = equation   
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
        """
        To use the data_integration method, one must provide the data in an array form. 
        """
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
# Testing area
###############################################################################

import parser as parser

formula = "sin(x)*x**2"
code = parser.expr(formula).compile()
