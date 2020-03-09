# Done
import numpy as np

def altitude_in_meters(seconds):
    """
    This program calculates the distance
    how far away a satelite needs to be from 
    the surface of the earth in order to complete 
    the specified period writen in seconds
    """ 
    gravitational_constant = 6.67e-11
    mass_of_earth = 5.97e24
    radius_of_earth = 6371e3
    time = float(seconds)
    
    height_above_earth = (((gravitational_constant * mass_of_earth * time**2) / (4 * np.pi**2))**(1/3) - radius_of_earth)
    
    return height_above_earth

print(altitude_in_meters(input("Write the period of the satelite's orbit in seconds: ")))