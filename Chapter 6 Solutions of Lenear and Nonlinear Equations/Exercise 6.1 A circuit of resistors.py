# Done
import linearnonlinearsolver as lnl 
import numpy as np

matrix = np.array([[4,-1,-1,-1],
                  [-1,3,0,-1],
                  [-1,0,3,-1],
                  [-1,-1,-1,4]], float)
vector = np.array([5,0,5,0],float)

# loading the matrix and vector of solutions
system_of_equations = lnl.LinearEquations(matrix,vector)
solution = system_of_equations.gaussian_elimination()

print(solution)