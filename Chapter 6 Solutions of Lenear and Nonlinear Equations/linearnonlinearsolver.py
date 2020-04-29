import numpy as np 
class LinearEquations:
    def __init__(self,matrix_of_variables,column_of_variables):
        self.matrix = matrix_of_variables
        self.vector = column_of_variables # vector of answers
    
    def __pivot_matrix(self):
        A = self.matrix
        v = self.vector
        N = len(v)
        rows_count = 0
        print("==========")
        print("Original matrix")
        print(A)
        print("==========")
        while rows_count < N:
            for m in range(N):
                diagonal_test = A[m,m]
                if diagonal_test == 0. and m < (N):
                    A[[m,m+1]], A[[m+1, m]] = A[[m+1, m]], A[[m, m+1]]
                    print("==========")
                    print("Pivot:")
                    print(A)
                    print("==========")
                elif diagonal_test == 0. and m == (N-1):
                    A[[m,0]], A[[0, m]] = A[[0, m]], A[[m, 0]]
                    print("==========")
                    print("Pivot:")
                    print(A)
                    print("==========")
                elif diagonal_test != 0:
                    rows_count += 1
        print("==========")
        print("Final matrix:")
        print(A)
        print("==========")
        return A, v                

    def gaussian_elimination(self, need_pivot=False):
        # if matrix needs to be pivoted
        if need_pivot == True:
            A, v = self.__pivot_matrix()
        elif need_pivot == False:
            A = self.matrix
            v = self.vector
        N = len(v) # number of rows

        # Gaussian elimination
        for m in range(N):
            # Divide the diagonal element
            div = A[m,m]
            A[m,:] /= div
            v[m] /= div
            # substract from the lower rows
            for i in range(m+1,N):
                mult = A[i,m]
                A[i,:] -= mult*A[m,:]
                v[i] -= mult*v[m]
        # Backsubstraction
        x = np.empty(N,float)
        for m in range(N-1,-1,-1):
            x[m] = v[m]
            for i in range(m+1,N):
                x[m] -= A[m,i]*x[i]
        print("Answer:")
        return x



    