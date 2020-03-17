# Done
import numpy as np
import matplotlib.pyplot as plt
"""
This exercise asks to plot stm.txt which contains a grid of values from scanning tunneling
microscope measurements of the surface of silicon. Show the structure of the surface
of silicon clearly.
"""
silicon_surface_data = np.loadtxt(r"..\cpresources\stm.txt")

plt.imshow(silicon_surface_data,origin="lower")
plt.show()