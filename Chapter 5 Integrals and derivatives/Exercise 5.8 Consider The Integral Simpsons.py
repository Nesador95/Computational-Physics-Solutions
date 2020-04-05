# Done
import numpy as np 
import IntegrationMethods as IM 

equation = IM.equation("(sin(sqrt(100*x)))^2", ["x"])
print("Using adaptive integration")
integral = IM.SimpsonsRuleIntegration().adaptive_function_integration(equation,0,1,10e-6)

