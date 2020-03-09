# Done
import numpy as np
import matplotlib.pyplot as plt
"""
This Exercise asks to plot three functions:
the deltoid curve, the galilean_spiral, and Fey's function
to accomplish this more easily building a polar plot coordinate
converted was also asked for.
"""
# part a

def deltoid_curve(theta_limit):
    theta = np.linspace(0,2*np.pi,theta_limit)
    
    x = 2*np.cos(theta) + np.cos(2*theta)
    y = 2*np.sin(theta) - np.sin(2*theta)

    return x, y 

x,y = deltoid_curve(1000)

plt.plot(x,y)
plt.show()

# part b

def polar_plot_converter(r,theta_array):
    # x and y transformations from polar to cartesian
    x = r * np.cos(theta_array)
    y = r * np.sin(theta_array)
    return x, y

def galilean_spiral(theta_limit,theta_steps):
    
    theta = np.linspace(0,theta_limit,theta_steps)
    r = theta**2

    return r, theta

r,theta = galilean_spiral(10*np.pi, 100)
x, y = polar_plot_converter(r,theta)
plt.plot(x,y)
plt.show()

# part c

def feys_function(theta_limit,theta_steps):
    theta = np.linspace(0,theta_limit,theta_steps)
    r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5

    return r, theta

r,theta = feys_function(24*np.pi,10000)
x, y = polar_plot_converter(r,theta)

plt.plot(x,y)
plt.show()
