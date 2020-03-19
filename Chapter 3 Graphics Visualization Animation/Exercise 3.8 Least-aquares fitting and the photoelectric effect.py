# Done
import numpy as np 
import matplotlib.pyplot as plt 

###############################################################################
# Set up
###############################################################################

data = np.loadtxt(r"..\cpresources\millikan.txt")

class LeastSquareFit:

    def __init__(self,x_points,y_points):
        self.x = x_points
        self.y = y_points
    
    def __finding_m_and_c(self):
        Ex = (1/len(self.x))*sum(self.x)
        Ey = (1/len(self.y))*sum(self.y)
        Exx = (1/len(self.x))*sum(self.x**2)
        Exy = (1/len(self.x))*sum(self.x*self.y)

        m = (Exy - (Ex*Ey)) / (Exx - Ex**2) 
        c = ((Exx*Ey) - (Ex*Exy)) / (Exx - Ex**2)
        return m , c 

    def chi_square(self):
        m, c = self.__finding_m_and_c()
        chi = sum( ((m*self.x) +c-self.y)**2 )
        return chi
    
    def best_fit_line(self):
        m, c = self.__finding_m_and_c()
        best_y = m*self.x+c
        return self.x, best_y

###############################################################################
# Part a
###############################################################################

plt.scatter(data[:,0],data[:,1])
        
###############################################################################
# Part b & c
###############################################################################
    
millican_measurements = LeastSquareFit(data[:,0],data[:,1]) 
x,y = millican_measurements.best_fit_line()
plt.plot(x,y)

###############################################################################
# Part d
###############################################################################

# Photoelectric effect equation re-arranged to solve for Planck's constant

def photoelectric(Nu, voltage):
    V = voltage
    Phi = 8.171104858346687e-19 # work function value of gold in J
    e = -1.602e-19 # charge of an electron 
    plancks_constant_h = (e*(V+Phi)) / Nu
    plancks_constant_h = np.mean(plancks_constant_h)
    return plancks_constant_h

Plancks_constant_experimental = photoelectric(data[:,0], data[:,1])
Plancks_constant_best_fit = photoelectric(x,y)
Plancks_constant__accepted = 6.62607015e-34
print( Plancks_constant_experimental/Plancks_constant__accepted, Plancks_constant_best_fit/Plancks_constant__accepted)

