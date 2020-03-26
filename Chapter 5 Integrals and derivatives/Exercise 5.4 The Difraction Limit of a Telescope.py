# Done 
import numpy as np 
import matplotlib.pyplot as plt 
import IntegrationMethods as IM


###############################################################################
# Part a
###############################################################################

x_list = np.linspace(0,20,100)

# for J_0
m = 0
J_0_values = np.zeros_like(x_list)
index = 0
for x in x_list:
    Equation = IM.equation("cos({0}*theta - {1}*sin(theta))".format(m,x), ["theta"])
    value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,np.pi,1000)
    J_0_values[index] = (1/np.pi) * value
    index +=1

# for J_1
m = 1
J_1_values = np.zeros_like(x_list)
index = 0
for x in x_list:
    Equation = IM.equation("cos({0}*theta - {1}*sin(theta))".format(m,x), ["theta"])
    value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,np.pi,1000)
    J_1_values[index] = (1/np.pi) * value
    index +=1

# for J_2
m = 2
J_2_values = np.zeros_like(x_list)
index = 0
for x in x_list:
    Equation = IM.equation("cos({0}*theta - {1}*sin(theta))".format(m,x), ["theta"])
    value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,np.pi,1000)
    J_2_values[index] = (1/np.pi) * value
    index +=1


plt.plot(x_list,J_0_values)
plt.plot(x_list,J_1_values)
plt.plot(x_list,J_2_values)
###############################################################################
# Part b
###############################################################################


def intensity_of_light_eq(J, wavelenght,r_of_focal_plane_to_diffract_pattern):
    r = r_of_focal_plane_to_diffract_pattern
    k = (2*np.pi/wavelenght)
    I_r = ((J*(k*r)) / (k*r))**2
    return I_r

################# Grid maker for an image density plot ########################

side = 2e-6 # Side of the Square from 0 to the number desired here
points = 100 # Number of grid points along each side
spacing = side/points # Spacing of points

# calculating the position of the center(s) of the events
separation = 0 # disntance from center
x_event1 = side/2 + separation # x coordinates of event 1
y_event1 = side/2 + separation # y coordinates of event 1

# Array to store the height of each point
final_grid = np.empty([points,points], float)

# calculation of the values in the array 
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        # Below set up the mathematical expression to be calculated per point
        # Remember to account for the position of the event's origin
        Equation = IM.equation("cos({0}*theta - {1}*sin(theta))".format(0,np.sqrt((x-x_event1)**2 + (y-y_event1)**2)), ["theta"])
        value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,np.pi,1000)
        final_grid[i,j] = intensity_of_light_eq((1/np.pi)*value,500e-9,np.sqrt((x-x_event1)**2 + (y-y_event1)**2))

# Making the plot
plt.imshow(final_grid, origin="lower", extent=[0,side,0,side])
plt.show()
