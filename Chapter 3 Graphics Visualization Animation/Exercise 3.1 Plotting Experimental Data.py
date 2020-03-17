# Done
import numpy as np
import matplotlib.pyplot as plt

sun_spots_data = np.loadtxt(r"..\cpresources\sunspots.txt")

x = sun_spots_data[:, 0]
y = sun_spots_data[:, 1]

plt.plot(x,y)
plt.show()

# Only the first 1000 with running average

x_thousend = sun_spots_data[:1001, 0]
y_thousend = sun_spots_data[:1001, 1]

def Y_k_average(y):
    r = 5
    for m in range(-r,r+1):
        Yk_sum = y + m
    return (1/2*r) * Yk_sum
 
         
plt.plot(x_thousend, y_thousend)
plt.plot(x_thousend, Y_k_average(y_thousend))
plt.show()