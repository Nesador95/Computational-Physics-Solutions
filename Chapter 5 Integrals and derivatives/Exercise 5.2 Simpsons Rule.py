import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (2/np.sqrt(np.pi))*np.exp(-x**2)

def Simpsons_integration_function(start, stop, num_slices):

    bound_a = start
    bound_b = stop
    
    width = (bound_b - bound_a) / num_slices
    summation =  (function(bound_a) + function(bound_b))
    summation_even = 0
    summation_odd = 0

    for even in range(2, (num_slices), 2):
        summation_even += (function(bound_a + ( even * width)))
    summation_even = summation_even * 2
    for odd in range(1, (num_slices), 2):
        summation_odd += (function(bound_a + (odd * width)))
    summation_odd = summation_odd * 4
    
    summation += summation_odd + summation_even
    summation = (1/3)  * width * summation
    return summation

def Simpsons_integration_data(data):

    bound_a = data[0]
    bound_b = data[-1]
    
    width = (bound_b - bound_a) / len(data)
    summation =  (bound_a + bound_b)
    summation_even = 0
    summation_odd = 0

    for even in range(2, len(data), 2):
        summation_even += data[even]
    summation_even = summation_even * 2
    for odd in range(1, len(data), 2):
        summation_odd += data[odd]
    summation_odd = summation_odd * 4
    
    summation += summation_odd + summation_even
    summation = (1/3)  * width * summation
    return summation

#data_load
data_loaded = np.loadtxt(fname='Chapter 5/velocities.txt', dtype=float,usecols=1)
#execution
#answer = Simpsons_integration_function(0, 3, 1000)
bounds = np.linspace(-2,2,100) 
answer = []
for bound_b in range(len(bounds)):
    answer.append(Simpsons_integration_function(-2, bounds[bound_b], 100))

plt.plot(bounds, answer)
plt.show()
#print(answer)
#answer_data = Simpsons_integration_data(data_loaded)
#print(answer_data)