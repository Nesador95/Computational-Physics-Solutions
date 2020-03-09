
import numpy as np
import matplotlib.pyplot as plt

def Function(x):
    return x**4 - 2*x +1

def Trapesoid_integration(bound_a, bound_b, num_slices,function):

    width = (bound_b - bound_a) / num_slices
    summation = (function(bound_a) + function(bound_b))

    for portion in range(1, (num_slices)):
        summation += function(bound_a + portion * width)
    
    summation = 0.5*width

    return summation
np.trapz

def Trapesoid_integration_of_data(data):

    width = (data[-1] - data[0]) / len(data)
    summation = 0

    summation += 0.5 * width * data[0]
    summation += 0.5 * width * data[-1]
    for item in range(len(data)):
        summation += width * (data[item])
    summation = summation

    return summation

#data_load
data = np.loadtxt(fname='Chapter 5/velocities.txt', dtype=float,usecols=1)
data_time = np.loadtxt(fname='Chapter 5/velocities.txt', dtype=float,usecols=0)

#Execution of Trapesoidal rule
T = Trapesoid_integration_of_data(data)
print(T)

#Displacement
def displacement(data, data_time):
    distance = []
    for time_step in range(len(data)):
        distance.append(data[time_step]*data_time[time_step])
    return distance

displacement_for_plot = displacement(data,data_time)
#Ploting
plt.plot(data_time, displacement_for_plot, label='distance' )
plt.show()
plt.plot(data_time, data, label='time')
plt.show()
