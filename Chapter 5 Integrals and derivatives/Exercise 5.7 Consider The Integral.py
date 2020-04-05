# Done
import numpy as np 
import IntegrationMethods as IM 

###############################################################################
# part a
###############################################################################

equation = IM.equation("(sin(sqrt(100*x)))^2", ["x"])
print("Using adaptive integration")
integral = IM.TrapeziumRuleIntegration().adaptive_function_integration(equation,0,1,10e-6)
###############################################################################
# part b
###############################################################################

print("Using Romberg integration")
romberg_integral = IM.TrapeziumRuleIntegration().romberg_function_integration(equation,0,1,10e-6)