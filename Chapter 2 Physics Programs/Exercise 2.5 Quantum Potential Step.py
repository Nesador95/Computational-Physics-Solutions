# Done

import numpy as np

def k_1_vector(mass, energy, h_bar):
    
    k_1 = np.sqrt( 2 * mass * energy ) / h_bar
    return k_1

def k_2_vector(mass, energy, potential_energy_barrier_V, h_bar):

    k_2 = np.sqrt( 2 * mass * ( energy - potential_energy_barrier_V )  ) / h_bar 
    return k_2

def probability_transmission(mass, energy, potential_energy_barrier_V, h_bar):

    k_1 = k_1_vector(mass, energy, h_bar)
    k_2 = k_2_vector(mass, energy, potential_energy_barrier_V, h_bar)

    T = ( 4 * k_1 * k_2 ) / ( k_1 + k_2 )**2
    return T

def probability_reflection(mass, energy, potential_energy_barrier_V, h_bar):

    k_1 = k_1_vector(mass, energy, h_bar)
    k_2 = k_2_vector(mass, energy, potential_energy_barrier_V, h_bar)

    R = ( ( k_1 - k_2 ) / ( k_1 + k_2 ) )**2
    return R

def quantum_potential_step_calculator(mass, energy, potential_energy_barrier_V):
    h_bar = 6.582119514e-16

    T = probability_transmission(mass, energy, potential_energy_barrier_V, h_bar)
    R = probability_reflection(mass, energy, potential_energy_barrier_V, h_bar) 

    return "The probability of transmission of this particle and barrier combination is %f, and the probability of reflection is %f" % (T, R)


##########################################################################################################


print(quantum_potential_step_calculator(float(input("please give the particle's mass in kg ")), float(input('please give the energy of the particle in eV ')), float(input("please give the energy of the potential energy barrier in eV "))))






