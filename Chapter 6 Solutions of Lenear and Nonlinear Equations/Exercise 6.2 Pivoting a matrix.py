# Done
import numpy as np 
import linearnonlinearsolver as lnl 

###############################################################################
# part a
###############################################################################

matrix = np.array([[4,-1,-1,-1],
                  [-1,3,0,-1],
                  [-1,0,3,-1],
                  [-1,-1,-1,4]], float)
vector = np.array([5,0,5,0],float)

# loading the matrix and vector of solutions
system_of_equations = lnl.LinearEquations(matrix,vector)
solution = system_of_equations.gaussian_elimination()
print(solution)
# pivoting matrix and demonstrate I get the same answer

matrix = np.array([[4,-1,-1,-1],
                  [-1,3,0,-1],
                  [-1,0,3,-1],
                  [-1,-1,-1,4]], float)
vector = np.array([5,0,5,0],float)

system_of_equations = lnl.LinearEquations(matrix,vector)
solution = system_of_equations.gaussian_elimination(True)
print(solution)

###############################################################################
# part b
###############################################################################

# Matrix that must be pivoted in order to give an answer 
# or it will break the program.
matrix_b = np.array([[0,1,4,1],
                  [3,4,-1,-1],
                  [1,-4,1,5],
                  [2,-2,1,3]], float)
vector_b = np.array([-4,3,9,7],float)

system_of_equations_b = lnl.LinearEquations(matrix_b,vector_b)
solution_b = system_of_equations_b.gaussian_elimination(True)
print(solution_b)