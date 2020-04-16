# Done
# part a is a pen and paper problem.
import numpy as np 
import IntegrationMethods as IM 
import matplotlib.pyplot as plt 
###############################################################################
# part b
###############################################################################
def period_of_anharmonic(m, Integral):
    I = Integral
    return np.sqrt(8*m)*I

# Integral set up
Amplitude = np.linspace(0,2,200) # upper boundary of integral
x,w = IM.GaussianQuadrature().gaussxw(20)
Time = np.zeros_like(Amplitude)
m = 1
# Integration Process
index = 0
for a in Amplitude:
    equation = IM.equation("1/sqrt({0}^4-x^4)".format(a),["x"])
    I = IM.GaussianQuadrature().apply_integration(equation,0,a,x,w)
    Time[index] = period_of_anharmonic(m,I)
    index += 1

plt.plot(Amplitude,Time)
plt.title("Period v. Amplitude for Anharmonic Oscillator")
plt.ylabel("Period")
plt.xlabel("Amplitude")
plt.show()

# part c is conceptual question
