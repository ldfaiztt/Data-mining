# Author: Sheng Li
# Matrix:
# 		M	N	P	Q	R
#	A	1	2	3	4	5
#	B	2	3	2	5	3
#	C	5	5	5	3	2

import numpy as np

# Matrix containing raw movie ratings by users A, B and C
rawRating = np.array([[1,2,3,4,5],
              [2,3,2,5,3],
              [5,5,5,3,2]])

# Matrix containing average movie ratings by users A, B and C
userAvg = np.array([[3,3,3,3,3],
             [3,3,3,3,3],
             [4,4,4,4,4]])

# the normalized movie ratings for users A, B and C
normalRating = rawRating - userAvg
print "Normalized user ratings: "
print normalRating

#Normalized user ratings: 
#[[-2 -1  0  1  2]
# [-1  0 -1  2  0]
# [ 1  1  1 -1 -2]]

movieAvg = np.array([[-2.0/3, 0, 0, 2.0/3, 0],
            [-2.0/3, 0, 0, 2.0/3, 0],
            [-2.0/3, 0, 0, 2.0/3, 0]])

normalizedScore = normalRating - movieAvg
print "Normalized movie scores: "
print normalizedScore

#Normalized movie scores: 
#[[-1.33333333 -1.          0.          0.33333333  2.        ]
# [-0.33333333  0.         -1.          1.33333333  0.        ]
# [ 1.66666667  1.          1.         -1.66666667 -2.        ]]