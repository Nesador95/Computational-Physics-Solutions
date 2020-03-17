# Done
import numpy as np
import matplotlib.pyplot as plt

silicon_surface_data = np.loadtxt(r"..\cpresources\stm.txt")

plt.imshow(silicon_surface_data,origin="lower")
plt.show()