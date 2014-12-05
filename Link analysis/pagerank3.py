# Author: Sheng Li
# Question 3
import numpy as np

# Adjacency matrix
# m3 = [ 0,  0, 1]
#	   [0.5, 0, 0]
#	   [0.5, 1, 0]

m3 = np.matrix([[0, 0, 1],[0.5, 0, 0],[0.5, 1, 0]])
beta = 1
r = np.matrix([1,1,1]).T

for i in range(100):
    r = m3.dot(r)
    print i+1
    print r

print "Final PageRank: \n" + str(r)