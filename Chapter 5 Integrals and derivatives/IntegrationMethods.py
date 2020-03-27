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

    def function_integration(self,equation, bound_a, bound_b, num_slices, error=False):
        """    
        To use this method, define the equation first with
        the method equation, then pass the equation to this method,
        provide the bounderies and the number of slices 
        for the trapezoidal rule to execute. 
        
        The error optinal parameter should be turned on only 
        if you need the estimated error to be returned for the calculation.
        Note that this might make the calculation take longer.

        example:
        function_integration(equation, 0, 2, 10)
        """
        if error==False:
            f = equation
            width = (bound_b - bound_a) / num_slices
            summation = 0.5*(f(bound_a) + f(bound_b))
            for portion in range(1, num_slices):
                summation += f(bound_a + portion * width)
            summation *= width
            return summation

        elif error==True:
            f = equation
            width = (bound_b - bound_a) / num_slices
            summation1 = 0.5*(f(bound_a) + f(bound_b))
            for portion in range(1, num_slices):
                summation1 += f(bound_a + portion * width)
            summation1 *= width
            # Integrating a second time with half the slices to calculate error 
            num_slices = num_slices//2
            width = (bound_b - bound_a) / num_slices
            summation2 = 0.5*(f(bound_a) + f(bound_b))
            for portion in range(1, num_slices):
                summation2 += f(bound_a + portion * width)
            summation2 *= width

            error = (1/3) * (summation2-summation1)
            return summation1, error

        
        
    
    def data_integration(self, data, error=False):
        """
        To use the data_integration method, one must provide the data in an array form.
        """
        if error==False:
            N_slices = len(data)
            width = (data[-1] - data[0]) / N_slices
            summation = 0.5*(data[0] + data[-1])
            for datum in range(1,N_slices):
                summation += (data[datum])
            summation *= width
            return summation
        elif error==True:
            N_slices = len(data)
            width = (data[-1] - data[0]) / N_slices
            summation1 = 0.5*(data[0] + data[-1])
            for datum in range(1,N_slices):
                summation1 += (data[datum])
            summation1 *= width
            # Integrating a second time with half the slices to calculate error
            half_data_points = data[::2]
            N_slices = len(half_data_points)
            width = (half_data_points[-1] - half_data_points[0]) / N_slices
            summation2 = 0.5*(half_data_points[0] + half_data_points[-1])
            for datum in range(1,N_slices):
                summation2 += (data[datum])
            summation2 *= width
            error = (1/3) * (summation2 - summation1)
            return summation1, error

class SimpsonsRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using Simpson's Rule integration method. note that Simpson's Rule requires
    an even number of steps to work properly.

    The maximum amount of slices needed to achieve maximum accuracy with sympsons
    rule is 10000. anything more and rounding error is dominant and a waist
    of computation.
    """
    def function_integration(self,equation, bound_a, bound_b, num_slices, error=False):
        """    
        To use this method, define the equation first with
        the method equation, then pass the equation to this method,
        provide the bounderies and the number of slices 
        for Simpson's rule to execute.

        example:
        function_integration(equation, 0, 2, 10)
        """
        if error==False: 
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

        elif error==True:
            f = equation   
            width = (bound_b - bound_a) / num_slices
            summation1 =  (f(bound_a) + f(bound_b))
            summation_even = 0
            summation_odd = 0
            for odd in range(1, num_slices, 2):
                summation_odd += (f(bound_a + (odd*width)))
            summation_odd *=  4
            for even in range(2, num_slices, 2):
                summation_even += (f(bound_a + (even*width)))
            summation_even *= 2
            summation1 += summation_odd + summation_even
            summation1 *= (1/3) * width

            num_slices = num_slices//2 
            width = (bound_b - bound_a) / num_slices
            summation2 =  (f(bound_a) + f(bound_b))
            summation_even = 0
            summation_odd = 0
            for odd in range(1, num_slices, 2):
                summation_odd += (f(bound_a + (odd*width)))
            summation_odd *=  4
            for even in range(2, num_slices, 2):
                summation_even += (f(bound_a + (even*width)))
            summation_even *= 2
            summation2 += summation_odd + summation_even
            summation2 *= (1/3) * width
            
            error = (1/15) * (summation1 - summation2)
            return summation1, error

    def data_integration(self, data, error=False):
        """
        To use the data_integration method, one must provide the data in an array form. 
        """
        if error==False:
            N_slices = len(data)
            bound_a = data[0]
            bound_b = data[-1]
            width = (bound_b - bound_a) / N_slices
            summation =  (bound_a + bound_b)
            summation_even = 0
            summation_odd = 0
            for odd in range(1, N_slices, 2):
                summation_odd += data[odd]
            summation_odd *= 4
            for even in range(2, N_slices, 2):
                summation_even += data[even]
            summation_even *= 2
            summation += summation_odd + summation_even
            summation *= (1/3) * width
            return summation

        elif error==True:
            N_slices = len(data)
            bound_a = data[0]
            bound_b = data[-1]
            width = (bound_b - bound_a) / N_slices
            summation1 =  (bound_a + bound_b)
            summation_even1 = 0
            summation_odd1 = 0
            for odd in range(1, N_slices, 2):
                summation_odd1 += data[odd]
            summation_odd1 *= 4
            for even in range(2, N_slices, 2):
                summation_even1 += data[even]
            summation_even1 *= 2
            summation1 += summation_odd1 + summation_even1
            summation1 *= (1/3) * width

            half_data_points = data[::2]
            N_slices = len(half_data_points)
            bound_a = half_data_points[0]
            bound_b = half_data_points[-1]
            width = (bound_b - bound_a) / N_slices
            summation2 =  (bound_a + bound_b)
            summation_even2 = 0
            summation_odd2 = 0
            for odd in range(1, N_slices, 2):
                summation_odd2 += half_data_points[odd]
            summation_odd2 *= 4
            for even in range(2, N_slices, 2):
                summation_even2 += half_data_points[even]
            summation_even2 *= 2
            summation2 += summation_odd2 + summation_even2
            summation2 *= (1/3) * width

            error = (1/15) * (summation2 - summation1)
            return summation1, error

