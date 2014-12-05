import numpy as np

# Adjacency matrix
# m1 = [ 0,  0, 0]
#	   [0.5, 0, 0]
#	   [0.5, 1, 1]	   

m1 = np.matrix([[0, 0, 0],[0.5, 0, 0],[0.5, 1, 1]])
beta =0.7

# r = beta * m1 * r + ((1-beta)/N) 

def r_p(r):
	return beta * m1 * r + np.matrix([0.1,0.1,0.1]).T
	
r = np.matrix([1.0/3,1.0/3,1.0/3]).T

for i in range(1000):
	r = r_p(r)
print "Final PageRank: \n" + str(r*3)  
print "\n"

a = r[0] * 3
b = r[1] * 3
c = r[2] * 3

print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'a + b = ', a + b
print 'b + c = ', b + c
print 'a + c = ', a + c