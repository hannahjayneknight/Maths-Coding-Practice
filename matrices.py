# Python Programming illustrating 
# numpy.identity method 
  
import numpy as geek 
  
# 2x2 matrix with 1's on main diagnol 
b = geek.identity(2, dtype = float) 
print("Matrix b : \n", b) 

a = geek.identity(4) 
print("\nMatrix a : \n", a)

#this inverses the matrix A
import numpy as np

A = [[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]
Ainv = np.linalg.inv(A)

print("\nMatrix A Inverse : \n", Ainv)

    