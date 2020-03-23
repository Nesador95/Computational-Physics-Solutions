# Not Done 
import numpy as np 
import matplotlib.pyplot as plt 
import IntegrationMethods as IM 

###############################################################################
# Part a
###############################################################################

x_list = np.linspace(0,20,21)

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
# Part b NOT FINISHED YET!!
###############################################################################


def polar_plot_converter(r,theta_array):
    # x and y transformations from polar to cartesian
    x = r * np.cos(theta_array)
    y = r * np.sin(theta_array)
    return x, y


def intensity_of_light_eq(J, wavelenght,r_of_focal_plane_to_diffract_pattern):
    r = r_of_focal_plane_to_diffract_pattern
    k = (2*np.pi/wavelenght)
    I_r = ((J*(k*r)) / (k*r))**2
    return I_r


r_distance = np.linspace(0,1e-6,100)
theta_steps = 100
angles = np.linspace(0,2*np.pi,theta_steps)

for_j0x = []
for_j0y = []

for_j1x = []
for_j1y = []

for_j2x = []
for_j2y = []

m = 0
for r in r_distance:
    # calculating each point
    for angle in angles:
        x,y = polar_plot_converter(r, angle)
        # calculating J on at each point

        Equation = IM.equation("cos({0}*theta - {1}*sin(theta))".format(m,x), ["theta"])
        value = IM.SimpsonsRuleIntegration().function_integration(Equation,0,np.pi,1000)
        for_j0x.append(intensity_of_light_eq((1/np.pi)*value,500e-9,x))
        for_j0y.append(intensity_of_light_eq((1/np.pi)*value,500e-9,y))


    #for_j1.append(intensity_of_light_eq(J_1_values,500e-9,r))
    #for_j2.append(intensity_of_light_eq(J_2_values,500e-9,r))

j0 = [for_j0x, for_j0y] 
plt.imshow(j0)