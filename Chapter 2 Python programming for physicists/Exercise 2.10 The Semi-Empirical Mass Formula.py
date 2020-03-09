# Done
import numpy as np
"""
This program gives the binding energy for the corresponding atom, binding energy per nucleon,
the value of A of the most stable nucleus and its binding energy per nucleon.
"""
# Using A and Z get binding energy of the atom

def AZ_binding_energy(mass_number_A, atomic_number_Z): 
    Z = atomic_number_Z
    A = mass_number_A
    
    # Electron-volt constants
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    if A % 2 != 0:
        a_5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a_5 = 12.0
    elif A % 2 == 0 and Z % 2 != 0:
        a_5 = -12.0
    
    # Binding energy formula
    B = a_1*A - a_2*A**(2/3) - a_3*(Z**2/A**(1/3)) - a_4*((A - 2*Z)**2/A) +(a_5/A**(1/2))

    # Binding energy per nucleon
    B_per_nucleon = B/A
    return B, B_per_nucleon
print(AZ_binding_energy(58,28))

# most stable nucleon finder using only Z

def Z_binding_energy_range(atomic_number_Z): 
    Z = atomic_number_Z
    
    # Electron-volt constants
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    
    
    A_list = list(range(Z,3*Z+1))
    binding_energies = []
    bin_per_nucleai = []
    for A in A_list:
        if A % 2 != 0:
            a_5 = 0
        elif A % 2 == 0 and Z % 2 == 0:
            a_5 = 12.0
        elif A % 2 == 0 and Z % 2 != 0:
            a_5 = -12.0
        # Binding energy formula
        B = a_1*A - a_2*A**(2/3) - a_3*(Z**2/A**(1/3)) - a_4*((A - 2*Z)**2/A) +(a_5/A**(1/2))
        binding_energies.append(B)
        bin_per_nucleai.append(B/A)

    most_stable = max(bin_per_nucleai)
    A_of_most_stable = A_list[binding_energies.index(max(binding_energies))]
    
    return most_stable, A_of_most_stable, binding_energies

print(Z_binding_energy_range(28))

# Max value of all values of Z

def energy_range_for_all_Zs(): 
    Z_list = list(range(1,101))
    # Electron-volt constants
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    
    All_values_of_each_Z = []
    All_values_of_each_A = []
    All_values_of_each_B = []
    max_binding_energy_per_nucleon = []

    for Z in Z_list:
        A_list = list(range(Z,3*Z+1))
        current_Z = 0
        current_A = 0
        current_B = 0
        current_B_A = 0
        for A in A_list:
            if A % 2 != 0:
                a_5 = 0
            elif A % 2 == 0 and Z % 2 == 0:
                a_5 = 12.0
            elif A % 2 == 0 and Z % 2 != 0:
                a_5 = -12.0
            # Binding energy formula
            B = a_1*A - a_2*A**(2/3) - a_3*(Z**2/A**(1/3)) - a_4*((A - 2*Z)**2/A) +(a_5/A**(1/2))
            
            if B/A > current_B_A:
                current_Z = Z
                current_A = A
                current_B = B
                current_B_A = B/A
        
        All_values_of_each_A.append(current_A)
        All_values_of_each_Z.append(current_Z)
        All_values_of_each_B.append(current_B)
        max_binding_energy_per_nucleon.append(current_B_A)


    return All_values_of_each_Z, All_values_of_each_A, All_values_of_each_B, max_binding_energy_per_nucleon

print(energy_range_for_all_Zs())