# Done

import numpy as np
import matplotlib.pyplot as plt

def constant_c(xy_limits, N_for_NxN_grid):
    x = np.linspace(-xy_limits[0],xy_limits[1],N_for_NxN_grid, dtype=np.float64) # x values array
    y = np.linspace(-xy_limits[2],xy_limits[3],N_for_NxN_grid, dtype=np.float64) # y values array
    c = x + y[:,None]*1j # complex constant c built from x & y
    return x, y, c

def mandelbrot_set(xy_limits,N_for_NxN_grid,max_iterations):
    
    x,y,c = constant_c(xy_limits, N_for_NxN_grid)
    final_grid = np.zeros(c.shape)
    z = np.zeros(c.shape, dtype=np.complex64)

    for iteration in range(max_iterations):
        step = np.less(z.real*z.real + z.imag*z.imag, 4.0)
        final_grid[step] = iteration
        z[step] = z[step]**2 + c[step]
    final_grid[final_grid == max_iterations-1] = 0
    return x,y,final_grid.T

x,y,final = mandelbrot_set([-0.74877,0.06505,0.06510,-0.74872],2048,100)

plt.imshow(final,origin="lower",cmap="PRGn")
plt.show()
###############################################################################
# The suggested bounds and code optimization advice came from JeanFrancoisPuget
# from his blog post "How To Quickly Compute The Mandelbrot Set In Python" at
# the IBM community blogs:
# https://www.ibm.com/developerworks/community/blogs/jfp/entry/How_To_Compute_Mandelbrodt_Set_Quickly?lang=en
# his work made the mendelbrot a lot easier to understand and his advice
# permiates most parts of the final code I have here.