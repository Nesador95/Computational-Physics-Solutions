# Done
import numpy as np 
import IntegrationMethods as IM 
import matplotlib.pyplot as plt 

# Set up of equation

def intensity_of_wave_after_event(I_0,C,S):
    return (I_0/8) * ( (2*C+1)**2 + (2*S+1)**2)

def u(x,lambd,z):
    return x*np.sqrt(2/(lambd*z))

equation_C = IM.equation("cos(0.5*pi*t^2)",["t"])
equation_S = IM.equation("sin(0.5*pi*t^2)",["t"])


# constants and variables
x_values = np.linspace(-5,5,200)
lambd = 1 # meters
z = 3 # meters in z direction
I_0 = 10 # sound intensity before event
index = 0
I_after = np.zeros_like(x_values)
# Set up of Integral
x,w = IM.GaussianQuadrature().gaussxw(50)
for i in x_values:
    u_varaible = u(i,lambd,z)
    C = IM.GaussianQuadrature().apply_integration(equation_C,0,u_varaible,x,w)
    S = IM.GaussianQuadrature().apply_integration(equation_S,0,u_varaible,x,w)
    I_after[index] = intensity_of_wave_after_event(I_0,C,S)
    index +=1

plt.plot(x_values,I_after)
plt.title("Diffraction of Sound Around an Edge")
plt.xlabel("x axis (m)")
plt.ylabel("z axis (m)")

