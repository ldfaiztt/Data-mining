#Author: Sheng Li

import numpy as np

# Consider the diagonal matrix M
M = [[1, 0, 0],
     [0, 2, 0],
     [0, 0, 0]]

# Compute its Moore-Penrose pseudoinverse
Minv = np.linalg.pinv(M)

print "Moore-Penrose pseudoinverse of matrix M: "
print Minv