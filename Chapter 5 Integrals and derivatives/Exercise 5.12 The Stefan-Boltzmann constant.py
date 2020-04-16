# Done
# part a is a pen and paper problem
import numpy as np 
import IntegrationMethods as IM 

###############################################################################
# part b
###############################################################################

def radiation_per_unit_area_by_bbody(T,integral_answer):
    I = integral_answer
    k = 1.380649e-23 # Boltzmann constant SI
    c = 299792458 # speed of light SI
    h = 6.62607015e-34/(2*np.pi) # h bar (Planck's constant over 2pi)

    return (k**4*T**4)/(4*np.pi**2*c**2*h**3) * I

# Set up of integral
# change of variables from x to z to account for infinite range
integral = IM.equation("(1/(1-z)^2) * ( (z^3/(1-z)^3) / (e^(z/(1-z))-1) )", ["z"])
x,w = IM.GaussianQuadrature().gaussxw(50)
integration = IM.GaussianQuadrature().apply_integration(integral,0.0,1.0,x,w)
result = radiation_per_unit_area_by_bbody(300,integration)

###############################################################################
# part c
###############################################################################
# calculating the Stefan-Boltzmann value from the equation result above

def Stefan_Boltzmann(radiation,T):
    return radiation/T**4

# accepted value for Stefan-Boltzmann (watts per square meter kelvin to the fourth)
accepted = 5.6703744191844e-8
# same temperature T as used above
print(Stefan_Boltzmann(result,300))
print(accepted)
print("percentage accuracy: " + str((Stefan_Boltzmann(result,300)/accepted) * 100)+ "%")