from Equation import Expression
# Needs better documentation
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
            
class GaussianQuadrature:

    def __init__(self,equation,integrating_variables, bounds_a,bounds_b):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.int_var = integrating_variables

    def __for_polynomial(self,degree):
        """
        Returns the optimal amount of points for a polynomial
        """
        return np.ceil((degree+1)/2)

    def gaussxw(self,is_polynomial=False,N_points):
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
        