# Author: Sheng Li
# Find the vector that is orthogonal to the vector [1,2,3]
import numpy as np

M = np.array([[0, 2, -1],
              [-3, 4, -2],
              [-1, -1, 1],
              [-4, 2, -1]])

Y = np.transpose(np.array([1, 2, 3]))
A = np.dot(M, Y)

print A
#[ 1 -1  0 -3]
