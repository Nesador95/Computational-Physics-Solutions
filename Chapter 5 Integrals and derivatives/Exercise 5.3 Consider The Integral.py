# Done
import numpy as np
import matplotlib.pyplot as plt 
import IntegrationMethods as IM

Equation = IM.equation("1/e**(t^2)", ["t"])
values_of_x = np.array(np.arange(0,3,0.1))
values_of_Ex = np.zeros_like(values_of_x)
index = 0

for bound_b in values_of_x:
    value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,bound_b,100) 
    values_of_Ex[index]= value
    index += 1

plt.plot(values_of_x,values_of_Ex)