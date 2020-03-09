# Done
import numpy as np 
# earts L1 = 1.4710e11 v1 = 3.0287e4
# halley L1 = 8.7830e10 v1 = 5.4529e4

'''
This program calculates the orbit of bodies orbiting the Sun by providing the perihelion 
and the velocity at the perihelion. (If you wish to do another body other than the sun as 
the center of orbit, go to "velocity_aphelion" and change the mass of the star.)
''' 

def velocity_aphelion(perihelion, velocity_perihelion):
    star_mass = 1.9891e30
    Newton_gravitational_constant = 6.6738e-11

    first_term = ((2*Newton_gravitational_constant*star_mass) / (velocity_perihelion*perihelion))
    second_term_1 = ((2*Newton_gravitational_constant*star_mass) / (velocity_perihelion*perihelion))
    second_term_2 = (-4 * (velocity_perihelion**2 - ((2 * Newton_gravitational_constant * star_mass) / (perihelion)) ) )

    v2 = (first_term - np.sqrt(second_term_1**2 - second_term_2 )) / 2
    print(v2)
    return v2 

def aphelion(perihelion,velocity_perihelion, velocity_aphelion):
    L2 = (perihelion * velocity_perihelion) / velocity_aphelion
    return L2

def Semimajor_axis(perihelion, aphelion):
    a = (1/2) * (perihelion + aphelion)
    return a

def Semiminor_axis(perihelion,aphelion):
    
    b = np.sqrt(abs(perihelion * aphelion))
    return b

def Orbital_period(s_major, s_minor, perihelion, velocity_perihelion):
    T = (2 * np.pi * s_major * s_minor ) / (perihelion * velocity_perihelion)
    return T

def Orbital_eccentricity(perihelion,aphelion):

    e = (aphelion - perihelion) / (aphelion + perihelion)
    return e

def Planetary_orbits(perihelion, velocity_perihelion):
    
    v2 = float(velocity_aphelion(perihelion, velocity_perihelion))
    L2 = float(aphelion(perihelion, velocity_perihelion, v2 ))
    s_major = float(Semimajor_axis(perihelion, L2))
    s_minor = float(Semiminor_axis(perihelion, L2))
    period = float(Orbital_period(s_major, s_minor, perihelion, velocity_perihelion))
    eccentricity = float(Orbital_eccentricity(perihelion, L2))

    print("aphelion: %f \n velocity at aphelion: %f \n orbital period: %f \n eccentricity: %f." % (L2, v2, period, eccentricity)) 

###############################################################################
# Execution 
###############################################################################
Planetary_orbits(float(input("please enter the prahelion of the orbit in m: ")), float(input("please enter the velocity at parahelion in m/s: ")))
