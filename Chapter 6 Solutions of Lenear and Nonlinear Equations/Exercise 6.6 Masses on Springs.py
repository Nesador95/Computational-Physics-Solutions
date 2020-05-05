import numpy as np 
from banded import banded
import vpython as vp 
import matplotlib.pyplot as plt 
###############################################################################
# Set up
###############################################################################

# constants 
N = 6
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k-m*omega**2

# Initial values of arrays
A = np.empty([3,N],float)
A[0,:] = -k
A[1,:] = alpha
A[2,:] = -k
A[1,0] = alpha - k
A[1,N-1] = alpha - k
v = np.zeros(N,float)
v[0] = C

# Solving the equation
x = banded(A,v,1,1)
print(x)
plt.plot(x)
plt.plot(x,"ko")
plt.show()

# Visualization

class mass:
    def __init__(self, position):
        self.body = vp.sphere(radius=0.1, pos=position, canvas=scene)
        self.position = position
    
    def vibrate(self,index, omega, time):
            new_position = vp.vector(x[index] *np.cos(omega * time), 0,0)
            self.body.pos = self.body.pos + new_position
            
caption = """This animation is a representation of a set of N identical masses in a row,
joined by identical linear sprngs."""
scene = vp.canvas(title="Vibration in a one dimentional system", caption= caption)
scene.select()

###############################################################################
# Rendering Stage
###############################################################################
initial_time = 0
x *= 10 # multiplying by 10 to increase scale for animation
mass_0 = mass(vp.vector(x[0]*np.cos(omega*initial_time),0,0))
mass_1 = mass(vp.vector(x[1]*np.cos(omega*initial_time),0,0))
mass_2 = mass(vp.vector(x[2]*np.cos(omega*initial_time),0,0))
mass_3 = mass(vp.vector(x[3]*np.cos(omega*initial_time),0,0))
mass_4 = mass(vp.vector(x[4]*np.cos(omega*initial_time),0,0))
mass_5 = mass(vp.vector(x[5]*np.cos(omega*initial_time),0,0))
###############################################################################
# Animation Stage
###############################################################################

for time in np.arange(0,200,.1):
    vp.rate(10)
    mass_0.vibrate(0,omega, time)
    mass_1.vibrate(1,omega, time) 
    mass_2.vibrate(2,omega, time)
    mass_3.vibrate(3,omega, time)
    mass_4.vibrate(4,omega, time) 
    mass_5.vibrate(5,omega, time)