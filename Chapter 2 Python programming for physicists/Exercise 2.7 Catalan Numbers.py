# Done
import numpy as np

def catalan_generator(max_number):
    n = 0
    C_n = 1
    C_list = [1.0]
    while C_n < max_number:
        
        C_n = ( (4*n + 2) / (n + 2) ) * C_n
        n += 1
        C_list.append(C_n)
    return C_list

print(catalan_generator(float(input("Up to what number should I calculate Catalan Numbers?"))))