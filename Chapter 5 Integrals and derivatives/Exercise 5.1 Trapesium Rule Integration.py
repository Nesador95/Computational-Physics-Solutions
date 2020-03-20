
import numpy as np
import matplotlib.pyplot as plt

class TrapesiumRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using the trapezium/trapezoidal integration method.

    To use the function_integration method, you must define the equation as 
    a global method with the name f(x) before execution, then provide the bounds 
    and the number of slices for the trapezoidal rule to execute.

    To use the data_integration method, one must provide the data in an array form. 
    The second argument for this method governs the accuracy of the answer; 
    if you want the maximum accuracy possible with the data set, 
    set it to the length of your data set; on the other hand if the dataset
    is very dense and maximum accuracy is too time-consuming,
    one can specify the number of slices less than the number of datum.
    """

    def function_integration(self, bound_a, bound_b, num_slices):
        width = (bound_b - bound_a) / num_slices
        summation = 0.5*(f(bound_a) + f(bound_b))
        for portion in range(1, num_slices):
            summation += f(bound_a + portion * width)
        summation *= width
        return summation
        
    
    def data_integration(self, data, number_of_slices):
        if number_of_slices > len(data):
            return "the resolution of the data does not support this level of detail\
                please specify a number smaller than the amount of datapoints or the lenght\
                    of data for maximum accuracy"
        else:    
            N_slices = number_of_slices
            width = (data[-1] - data[0]) / N_slices
            summation = 0.5*(data[0] + data[-1])
            for datum in range(len(data)):
                summation += (data[datum])
            summation *= width
            return summation

###############################################################################
# Test of function method 
###############################################################################
def f(x):
    return x**4 - 2*x +1

quadratic__function_test = TrapesiumRuleIntegration().function_integration(0,2,10000)
print(quadratic__function_test)

###############################################################################
# Part a     (test of data method)
###############################################################################

#loading data
data_loaded = np.loadtxt(r"../cpresources\velocities.txt")
time_data = data_loaded[:,0]
velocity_data = data_loaded[:,1]

#Execution of Trapesoidal rule in data
distance_traveled = TrapesiumRuleIntegration().data_integration(velocity_data,len(velocity_data))
print(distance_traveled)

###############################################################################
# Part b
###############################################################################

distance_traveled_per_unit_time = np.linspace(0,distance_traveled,len(time_data))

# Plotting
plt.plot(time_data,velocity_data) # original velocity plot
plt.plot(time_data,distance_traveled_per_unit_time) # distance traveled as a function of time
plt.show()