# Done
import numpy as np

a = np.array([1,2,3,4], int)
b = np.array([2,4,6,8], int)

# one can also apply sum, max, min and len to one dimentional
# one can also apply map and combine map with functions
print(list(map(np.sqrt,a))) 
old_list = list(range(100))
def f(x):
   return 2*x-1
new_list = list(map(f,old_list))

# multiplication /  division, including constants
print(b/a+1)
print(b/(a+1))
print(1/a)

# adding / substracting arrays
print(a+b)

# dot products
print(np.dot(a,b))

# Matrix operations
c = np.array([[1,3],[2,4]], int)
d = np.array([[4,-2],[-3,1]], int)
e = np.array([[1,2],[2,1]], int)

# the dot operation does mutiplication with matrices, if multiplying a vector:
# dot(c,v) treats the v vector as a column
# dot(v,c) treats the v vector as a row
print (np.dot(c,d)+2*e) 

# Instead of len for matrices, use size and shape
print(c.shape)
print(c.size)
