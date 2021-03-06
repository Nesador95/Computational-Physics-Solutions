from Equation import Expression
import numpy as np 
# Needs better documentation
# Needs to accomodate multivariable
# Needs to accomodate data integration
# Maybe they should be separated in to data and function classes each? 
class TrapesoidalRule:
    """
    Note: This requires that you install the package Equation: https://pypi.org/project/Equation/#description

    equation: takes in a string representing the mathematical equation

    example:
        equation = equation("x**4 - 2*x +1" , ["x"])
        or
        equation = equation("x^4 - 2*x +1" , ["x"])
        Note: 
        - Does not interprete np.exp, write instead e
        - Does not interprete 4**(-2), write instead 1/4**2
        to add letters as placeholders for constant or changing variable not
        being integrated 
        equation = equation("x^4*{0} - 2*x*{1}^2 +1".format(time_t,Boltzmann_const) , ["x"])

    integrating_variables: takes in a list of variables as strings i.e. ["x","y"].
                           Note: this objects integrates from left to right. by changing
                           the order of variables one may change the order of integration 
    bounds a & b: takes in a list of bounds i.e. bounds_a = [0,pi] & bounds_b = [3,2*pi]
                    must match the order of the variables entered.
    ===============
        When integrating over infinite ranges, there is a few 
        ways to set the equation:

        from 0 to inf:
        x = z/(1-z)
        dx = 1/(1-z)^2
        integral from 0 to 1

        from non-zero value a to inf:
        x = z/(1-z) + a
        dx = 1/(1-z)^2
        integral from 0 to 1
        Note: for integral from -inf to a, substitue z for -z

        from -inf to inf:
        x = tan(z)
        z = cos(z)^2
        integral from -pi/2 to pi/2
    ===============

    """
    def __init__(self,equation,integrating_variables, bounds_a,bounds_b ):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.int_var = integrating_variables
    
    def __f(self, equation, variables):
        f = Expression(equation, variables)
        return f

    def __perform_integral_without_error_one_var(self, num_slices):
        f = self.__f(self.equation,self.int_var)
        width = (self.bound_b - self.bound_a) / num_slices
        summation = 0.5*(f(self.bound_a) + f(self.bound_b))
        for portion in range(1, num_slices):
            summation += f(self.bound_a + portion * width)
        summation *= width
        return summation

    def __perform_integral_with_error_one_var(self, num_slices):
        summation1 = self.__perform_integral_without_error_one_var(num_slices)
        # Integrating a second time with half the slices to calculate error 
        num_slices = num_slices//2
        summation2 = self.__perform_integral_without_error_one_var(num_slices)
        error = (1/3) * (summation2-summation1)
        answer = [summation1, abs(error)]
        return answer
    
    def __perform_integral_adaptive_method(self, magnitude_of_tolerable_error):
        f = self.__f(self.equation,self.int_var)
        error_calculated = 100
        steps = 1
        print("=============================================")
        print(str(steps) + ' slice')
        I_i_1_less = self.__perform_integral_without_error_one_var(steps)
        I_i = 0
        print( 'estimated answer of '+ str(I_i_1_less) )
        while error_calculated > magnitude_of_tolerable_error:
            steps *= 2
            print(str(steps) + ' slices')
            h_i = (self.bound_b - self.bound_a) / steps #width of slices
            I_i = ( (1/2) * I_i_1_less ) + h_i*sum([f(self.bound_a+k*h_i) for k in range(1,steps,2)])
            error_calculated = abs((1/3) * (I_i - I_i_1_less))
            print('Answer: '+ str(I_i) + ' Error: '+ str(error_calculated))
            I_i_1_less = I_i
        print("=============================================")
        answer = [I_i, error_calculated]
        return answer
    # STILL WORKING ON IT
    def __perform_integral_without_error_two_var(self, num_slices):
        x,y = self.int_var[0], self.int_var[1]
        x_bound_a,y_bound_a = self.bound_a[0], self.bound_a[1]
        x_bound_b,y_bound_b = self.bound_b[0], self.bound_b[1]

        f = self.__f(self.equation,self.int_var)
        width = (self.x_bound_b - self.x_bound_a,) / num_slices
        summation = 0.5*(f(self.bound_a) + f(self.bound_b))
        for portion in range(1, num_slices):
            summation += f(self.bound_a + portion * width)
        summation *= width
        return summation

    def __romberg_function_integration(self, magnitude_of_tolerable_error):
        error_calculated = 100
        slices = 1 # the num of slices and also the row in Romberg triangle
        I_i_1_less = [] # the previous ith row of estimates (here the row is i = 1 but it updates)
        ith = 1 # number of estimations per row
        # first ith row
        R_1_1 = self.__perform_integral_without_error_one_var(slices)
        I_i_1_less.append(R_1_1)
        print("=============================================")
        print("Row " + str(ith) + " Amount of slices "+ str(slices))
        print(I_i_1_less)
        # iteration of all the other rows of estimations
        while error_calculated > magnitude_of_tolerable_error:
            slices *= 2
            ith += 1 
            I_i = []
            R_i_1 = self.__perform_integral_without_error_one_var(slices)
            I_i.append(R_i_1)
            for m in range(2,ith+1):
                error_calculated =abs( (1/(4**(m)-1)) * (I_i[-1] - I_i_1_less[I_i.index(I_i[-1])]) )
                R_i_m_plus_1 = I_i[-1] + ((1/(4**(m)-1)) * (I_i[-1] - I_i_1_less[I_i.index(I_i[-1])]))
                I_i.append(R_i_m_plus_1)
            I_i_1_less = I_i
            print("Row " + str(ith) + " Amount of slices "+ str(slices))
            print(I_i_1_less)
            print("Answer: " + str(I_i_1_less[-1]) + " Error at least: " + str(error_calculated)+ " + O(h_i^({}))".format(2*m+2))
        print("=============================================")
        answer = [I_i_1_less[-1], error_calculated]
        return answer
    
    def function_integration(self, num_slices=100, adaptive_method=False, romberg_method=False, magnitude_of_tolerable_error = 1e-6):
        """
        The three integration methods are:
        Trapezoidal with fixed slices (Default)
        Adaptive Trapezoidal integration
        Romberg integration
        They are mutually exclusive integration methods.
        __________________________________________________
        for integration with predetermined num of slices: 
            *It is Turned on by default        
            num_slices: the amount of slices used in the integration.
        __________________________________________________
        for integration with adaptive methd:
            adaptive_method: selects adaptive integration, turns off predetermined num of slices integration
            magnitude_of_tolerable_error: specify the error tolerable for calculation Default=1e-6
        __________________________________________________
        for romberg integration method:
            romberg_method: selects romberg integration method, turns off predetermined num of slices integration
            magnitude_of_tolerable_error: specify the error tolerable for calculation Default=1e-6
        """
        if adaptive_method==True:
            return self.__perform_integral_adaptive_method(magnitude_of_tolerable_error)
        elif romberg_method==True:
            return self.__romberg_function_integration(magnitude_of_tolerable_error)
        else:
            return self.__perform_integral_with_error_one_var(num_slices)
    # DOES NOT REALLY BELONG, THE ENTIRE CLASS NEEDS TO BE REMADE
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
# SAME AS TRAPESOIDALRULE           
class GaussianQuadrature:

    def __init__(self,equation,integrating_variables, bounds_a,bounds_b):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.int_var = integrating_variables

    def __f(self, equation, variables):
        f = Expression(equation, variables)
        return f

    def points_for_polynomial(self,degree):
        """
        Returns the optimal amount of points for a polynomial function
        """
        return np.ceil((degree+1)/2)

    def gaussxw(self, N_points):
        """
        Calculates the sample points and their weights for 
        gaussian integration.

        Avoid calling this function many times to avoid slowing down 
        your calculation. For many integrals over different domains
        of integration, call this method once to calculate 
        the sample points.


        Written by Mark Newman <mejn@umich.edu>, June 4, 2011.
        Used here with his permission.
        """
        N = N_points
        # Initial approximation to roots of the Legendre polynomial
        a = np.linspace(3,4*N-1,N)/(4*N+2)
        x = np.cos(np.pi*a+1/(8*N*N*np.tan(a)))

        # Find roots using Newton's method
        epsilon = 1e-15
        delta = 1.0
        while delta>epsilon:
            p0 = np.ones(N,float)
            p1 = np.copy(x)
            for k in range(1,N):
                p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
            dp = (N+1)*(p0-x*p1)/(1-x*x)
            dx = p1/dp
            x -= dx
            delta = max(abs(dx))

        # Calculate the weights
        w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

        return x,w
        
    def apply_integration(self,points_x, points_weights_w):
        """
        applies the Gaussian Quadrature integration method to the function
        specified. Requires points_x and points_weights_w that can be obtained from 
        the method 'gaussxw' 
        """
        f = f = self.__f(self.equation,self.int_var)

        # Setting up the points for the integration
        x = points_x
        w = points_weights_w
        a = self.bound_a
        b = self.bound_b
        xp,wp = 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

        # Performance of the integration
        solution = 0.0
        for k in range(len(x)):
            solution += wp[k]*f(xp[k])
        return solution
# SAME AS TRAPESOIDALRULE
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
    def __init__(self,equation,integrating_variables, bounds_a,bounds_b ):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.int_var = integrating_variables
    
    def __f(self, equation, variables):
        f = Expression(equation, variables)
        return f
    
    def __perform_integral_without_error_one_var(self, num_slices):
        int(num_slices)
        f = self.__f(self.equation,self.int_var)
        width = (self.bound_b - self.bound_a) / num_slices
        summation =  (f(self.bound_a) + f(self.bound_b))
        summation_even = 0
        summation_odd = 0
        for odd in range(1, num_slices, 2):
            summation_odd += (f(self.bound_a + (odd*width)))
        summation_odd *=  4
        for even in range(2, num_slices, 2):
            summation_even += (f(self.bound_a + (even*width)))
        summation_even *= 2
        summation += summation_odd + summation_even
        summation *= (1/3) * width
        return summation
    
    def __perform_integral_with_error_one_var(self, num_slices):
        int(num_slices)
        summation1 = self.__perform_integral_without_error_one_var(num_slices)
        # Integrating a second time with half the slices to calculate error 
        num_slices = num_slices//2
        summation2 = self.__perform_integral_without_error_one_var(num_slices)
        error = (1/15) * (summation1 - summation2)
        answer = [summation1, abs(error)]
        return answer
    
    def __perform_integral_adaptive_method(self, magnitude_of_tolerable_error= 1e-6):
        f = self.__f(self.equation,self.int_var)
        error_calculated = 100
        steps = 2
        h_i = (self.bound_b - self.bound_a) / steps
        S_1 =  (1/3) * (f(self.bound_a)+ f(self.bound_b) + 2*sum([f(self.bound_a+k*h_i) for k in range(2,steps,2)]) )
        T_1 = (2/3) * sum([f(self.bound_a+k*h_i) for k in range(1,steps,2)])
        print("=============================================")
        print(str(steps) + ' slices')
        I_i_1_less = h_i * (S_1 + 2*T_1)
        print('estimated answer of '+str(I_i_1_less))
        while error_calculated > magnitude_of_tolerable_error:
            steps *= 2
            print(str(steps) + ' slices')
            h_i = (self.bound_b - self.bound_a) / steps #width of slices
            T_i = (2/3) * sum([f(self.bound_a+k*h_i) for k in range(1,steps,2)])
            S_i = S_1 + T_1
            I_i = h_i * (S_i + 2*T_i)
            error_calculated = abs((1/15) * (I_i - I_i_1_less))
            print('Answer: '+str(I_i) + ' Error: '+ str(error_calculated))
            S_1 = S_i
            T_1 = T_i
            I_i_1_less = I_i
        print("=============================================")
        answer = [I_i, error_calculated]
        return answer

    def function_integration(self, num_slices=100, adaptive_method=False, magnitude_of_tolerable_error = 1e-6):
        if adaptive_method==True:
            return self.__perform_integral_adaptive_method(magnitude_of_tolerable_error)
        else:
            return self.__perform_integral_with_error_one_var(num_slices)
# THIS IS NOT FINNISHED
class FunctionDerivative:
    
    def __init__(self,equation,derivative_variable, bounds_a,bounds_b ):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.der_var = derivative_variable
    
    def __f(self, equation, variables):
        f = Expression(equation, variables)
        return f
    
    def __perform_derivative(self, size_slices):
        f = self.__f(self.equation,self.der_var)
        h = size_slices
        return (f())
    def __calculate_optimal_size_h(self):
        C = 1e-16 # value of error constant for python is typically this according to MArk Newman
        f = self.__f(self.equation,self.der_var)
        tentative_h = 1e-5
        dfdx = f(self.der_var+h/2)
        return  
    