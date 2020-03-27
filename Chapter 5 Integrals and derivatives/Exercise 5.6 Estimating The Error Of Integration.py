# Done 
import numpy as np 
import IntegrationMethods as IM 

equation = IM.equation("x**4 - 2*x + 1", ["x"])

IM.TrapeziumRuleIntegration().function_integration(equation,0,2,20,error=True)

IM.SimpsonsRuleIntegration().function_integration(equation,0,2,20,error=True)