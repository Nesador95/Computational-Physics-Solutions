# Done
import math as math
import numpy as np 
import matplotlib.pyplot as plt 
import IntegrationMethods as IM 

###############################################################################
# part a
###############################################################################

# quadratic potential well eq

def Hermite_polynomial(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return (2*x*Hermite_polynomial(n-1,x)) - (2*n*Hermite_polynomial(n-2,x))

def quantum_well(n,x):
    return (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) * np.e**(-x**2/2) * Hermite_polynomial(n,x)

x_values = np.linspace(-4,4,100)
list_of_solutions_of_n = []

for n in range(4):
    n_solution = []
    for x in x_values:
        solution = quantum_well(n,x)
        n_solution.append(solution)
    list_of_solutions_of_n.append(n_solution)

plt.plot(x_values,list_of_solutions_of_n[0])
plt.plot(x_values,list_of_solutions_of_n[1])
plt.plot(x_values,list_of_solutions_of_n[2])
plt.plot(x_values,list_of_solutions_of_n[3])

###############################################################################
# part b # gives the correct answer but i should be optimized
###############################################################################

n = 30
x_values = np.linspace(-10,10,100)
n_solution_30 = []
for x in x_values:
    solution = quantum_well(n,x)
    n_solution_30.append(solution)

plt.plot(x_values,n_solution_30)

###############################################################################
# part c
###############################################################################
# can't use my IntegrationMethods file properly since the library Equation
# does not support the feature I need to use funtions inside equations.
# Below I explicitly used Gaussian Quadrature. 

# integral set up
n = 5
def f(z):
    return (np.tan(z)**2 / np.cos(z)**2) * quantum_well(n,np.tan(z))**2
# Setting up the points for the integration
x,w = IM.GaussianQuadrature().gaussxw(100)
a = -(np.pi/2)
b = (np.pi/2)
xp,wp = 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

# Performance of the integration
solution = 0.0
for k in range(len(x)):
    solution += wp[k]*f(xp[k])
    
solution = np.sqrt(solution)

print(solution)
print(100 - ((solution/2.3 )* 100))
# The answer I get is 1.884144368046521
# the accepted answer is 2.3
# meaning that I'm off by about 18.08% 
# I need to find what the source of the error is or if it is just the integration error.

    