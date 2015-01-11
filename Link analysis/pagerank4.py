# Author: Sheng Li

import numpy as np

# Function to normalize all values so that the largest value is 1
def norm(Matrix):
	return Matrix/float(Matrix.max())

def estimate(L,h):
	# To estimate of the authority vector a = LTh
	a = L.T*h
	# Normalize a by dividing all values so the largest value is 1
	a = norm(a)
	# To estimate of the hubbiness vector h = La
	h = L*a
	# Normalize h by dividing all values so the largest value is 1
	h = norm(h)

	return a,h

# The vector h is (the transpose of) [1,1,1,1]
h = np.matrix([1,1,1,1]).T
# The link graph: 1->2; 1->3; 2->1; 3->4; 4->3
L = np.matrix([[0,1,1,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])

# After step 1
a,h = estimate(L,h)
print "After step 1:"
print "a:"
print a
print "hubbiness:" 
print h
print " "

# After step 2 (repeat of step 1)
a,h = estimate(L,h)
print "Final estimate:"
print "a:"
print a
print "hubbiness:" 
print h