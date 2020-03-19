# Done
import numpy as np 
import matplotlib.pyplot as plt

# r values from 1 to 4 in steps of 0.01 for 1000 iterations each
#  x = 1/2 is the starting value

r_values = np.arange(0,4,0.01)
x = np.full_like(r_values,0.5)

for i in r_values:
    x = r_values*x*(1-x)
    plt.scatter(r_values,x,s=0.1,color="black")
plt.ylabel("values of x")
plt.xlabel("values of r")
plt.show()

# Question a: based on the Feigenbaum plot, a fixed point looks like a location
# in the graph where all values converge into one value. A limit case looks like 
# a range of values that is bound to certain numbers. Chaos is when the plot seems
# to go at random.
# 
# Question b: I think the plot becomes disorderly at around the value 3.5   

        