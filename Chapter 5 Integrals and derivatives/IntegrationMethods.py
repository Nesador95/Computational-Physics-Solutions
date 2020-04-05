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
    or
    equation = equation("x^4 - 2*x +1" , ["x"])
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

    derivation of this method can be found in section 5.1.1 The Trapezoidal Rule
    from 'Computation Physics' by Mark Newman 
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
        int(num_slices)
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
            return summation1, abs(error)

    def adaptive_function_integration(self,equation, bound_a, bound_b, magnitude_of_tolerable_error):
        """
        This methods does the integration of a function and estimates the nessesary slices for the 
        desired accuracy. Keep in mind it cannot be infinetly accurate.
        It outputs the best estimate and its error. 
        """
        f = equation
        error_calculated = 100
        steps = 1
        print("=============================================")
        print(str(steps) + ' slice')
        I_i_1_less = self.function_integration(f,bound_a,bound_b,steps)
        print( 'estimated answer of '+ str(I_i_1_less) )
        while error_calculated > magnitude_of_tolerable_error:
            steps *= 2
            print(str(steps) + ' slices')
            h_i = (bound_b - bound_a) / steps #width of slices
            I_i = ( (1/2) * I_i_1_less ) + h_i*sum([f(bound_a+k*h_i) for k in range(1,steps,2)])
            error_calculated = abs((1/3) * (I_i - I_i_1_less))
            print('Answer: '+ str(I_i) + ' Error: '+ str(error_calculated))
            I_i_1_less = I_i
        print("=============================================")
        return I_i, error_calculated
    
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
            return summation1, abs(error)

    def romberg_function_integration(self,equation, bound_a, bound_b, magnitude_of_tolerable_error):
        """
        This methods does the integration of a function and estimates the nessesary slices for the 
        desired accuracy. This method is faster than the regular trapezoidal integration if the
        function is well behaved i.e. does not have singularities or is very noisy.
        If that is the case, then regular trapezium or Simpsons can give better results. 
        It outputs the best estimate and the error of the next to last estimate
        """
        f = equation
        error_calculated = 100
        slices = 1 # the num of slices and also the row in Romberg triangle
        I_i_1_less = [] # the previous ith row of estimates (here the row is i = 1 but it updates)
        mth = 1 # number of estimations per row
        # first ith row
        R_1_1 = self.function_integration(f,bound_a,bound_b,slices)
        I_i_1_less.append(R_1_1)
        print("=============================================")
        print("Row " + str(mth))
        print(I_i_1_less)
        # iteration of all the other rows of estimations
        while error_calculated > magnitude_of_tolerable_error:
            slices *= 2
            mth += 1 
            I_i = []
            R_i_1 = self.function_integration(f,bound_a,bound_b,slices)
            I_i.append(R_i_1)
            for m in range(2,mth+1):
                R_i_m_plus_1 = I_i[-1] + ((1/(4**(m)-1)) * (I_i[-1] - I_i_1_less[m-2]))
                I_i.append(R_i_m_plus_1)
                error_calculated =abs( (1/(4**(m)-1)) * (I_i[-1] - I_i_1_less[m-2]) )
            I_i_1_less = I_i
            print("Row " + str(mth))
            print(I_i_1_less)
            print("Answer: " + str(I_i_1_less[-1]) + " Error at least: " + str(error_calculated))
        print("=============================================")
        return I_i_1_less[-1], error_calculated

class SimpsonsRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using Simpson's Rule integration method. note that Simpson's Rule requires
    an even number of steps to work properly.

    The maximum amount of slices needed to achieve maximum accuracy with sympsons
    rule is 10000. anything more and rounding error is dominant and a waist
    of computation.

    derivation of this method can be found in section 5.1.2 Simpson's Rule
    from 'Computation Physics' by Mark Newman 
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
        int(num_slices)
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
            return summation1, abs(error)

    def adaptive_function_integration(self,equation, bound_a, bound_b, magnitude_of_tolerable_error):
        """
        This methods does the integration of a function and estimates the nessesary slices for the 
        desired accuracy. Keep in mind it cannot be infinetly accurate. 
        It outputs the best estimate and its error. 
        """
        f = equation
        error_calculated = 100
        steps = 2
        h_i = (bound_b - bound_a) / steps
        S_1 =  (1/3) * (f(bound_a)+ f(bound_b) + 2*sum([f(bound_a+k*h_i) for k in range(2,steps,2)]) )
        T_1 = (2/3) * sum([f(bound_a+k*h_i) for k in range(1,steps,2)])
        print("=============================================")
        print(str(steps) + ' slices')
        I_i_1_less = h_i * (S_1 + 2*T_1)
        print('estimated answer of '+str(I_i_1_less))
        while error_calculated > magnitude_of_tolerable_error:
            steps *= 2
            print(str(steps) + ' slices')
            h_i = (bound_b - bound_a) / steps #width of slices
            T_i = (2/3) * sum([f(bound_a+k*h_i) for k in range(1,steps,2)])
            S_i = S_1 + T_1
            I_i = h_i * (S_i + 2*T_i)
            error_calculated = abs((1/15) * (I_i - I_i_1_less))
            print('Answer: '+str(I_i) + ' Error: '+ str(error_calculated))
            S_1 = S_i
            T_1 = T_i
            I_i_1_less = I_i
        print("=============================================")
        return I_i, error_calculated

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
            return summation1, abs(error)

