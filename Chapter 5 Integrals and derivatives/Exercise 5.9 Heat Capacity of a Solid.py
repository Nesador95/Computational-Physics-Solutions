# Done
import numpy as np 
import matplotlib.pyplot as plt 
import IntegrationMethods as IM 

# Equation from Debye's Theory of solids
def heat_cap_of_solid_Cv(volume,density_atoms,Debye_temp,temperature, integra_solution):
    V = volume
    rho = density_atoms
    theta = Debye_temp
    T = temperature
    k = 1.380649e-23 # Boltzmann constant in J/K
    I = integra_solution
    return 9*V*rho*k*(T/theta)**3*I

###############################################################################
# part a
###############################################################################

# Initial values
Temp = 100 
rho = 6.022e28
Debye_theta = 428
N_steps = 50
Volume = 0.01
# Integral
equation = IM.equation("(x^4*e^x) / (e^x-1)^2", ["x"])
x,w = IM.GaussianQuadrature().gaussxw(N_steps)
bound_a = 0
bound_b = Debye_theta/Temp
integral = IM.GaussianQuadrature().apply_integration(equation,bound_a,bound_b,x,w)

# Computation of solution
solution = heat_cap_of_solid_Cv(Volume, rho, Debye_theta, Temp,integral)

print(solution)

###############################################################################
# part b
###############################################################################
# Initial values
rho = 6.022e28
Debye_theta = 428
N_steps = 50
Volume = 0.01 # cubic meters

Temp = np.linspace(5,500,500)
solution = np.zeros_like(Temp)
bound_a = 0

# Integral
equation = IM.equation("(x^4*e^x) / (e^x-1)^2", ["x"])
x,w = IM.GaussianQuadrature().gaussxw(N_steps)
index = 0
for i in Temp:
    bound_b = Debye_theta/i
    integral = IM.GaussianQuadrature().apply_integration(equation,bound_a,bound_b,x,w)
    # Computation of solution
    solution[index] = heat_cap_of_solid_Cv(Volume, rho, Debye_theta, i,integral)
    index += 1

plt.plot(Temp,solution)
plt.title("Heat Capacity of 0.01 Cubic Meters of Aluminium")
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity Cv")
plt.show()