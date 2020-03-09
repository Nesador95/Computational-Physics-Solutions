# Done
import numpy as np

"""This program calculates and prints the Madelung constant for sodium chloride."""

def madelung_constant(number_of_atoms, distance_between_atoms):
    e = -1.602176634e-19 # electron chanrge on coulomb
    e_0 = 8.8541878128e-12 # permittivity of the vacuum 
    V_total = 0 # total electric potential
    a = distance_between_atoms
    L = number_of_atoms

    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if i == 0 and j == 0 and k == 0:
                    continue
                elif abs(i+j+k) % 2 == 0:
                    V_total += e / (4*np.pi*e_0*a*np.sqrt(i**2+j**2+k**2))
                else:
                    V_total -= e / (4*np.pi*e_0*a*np.sqrt(i**2+j**2+k**2))
    
    M_constant = V_total*4*np.pi*e_0*a / e # Madelung constant
    return M_constant

# M constant for rocksalt = 1.748, lattice_distance = 0.000000000564 m or 5.64 angstroms
# Beware this code makes calculation depending on the size of the sodium chloride lattance (number_of_atoms*2)**3
print(madelung_constant(10,0.000000000564))
        
