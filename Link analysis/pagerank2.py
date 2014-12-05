import numpy as np

# Adjacency matrix
# m2 = [ 0,  0, 1]
#	   [0.5, 0, 0]
#	   [0.5, 1, 0]

m2 = np.matrix([[0, 0, 1],[0.5, 0, 0],[0.5, 1, 0]])
beta =0.85

def r_p(r):
	return beta * m2 * r + np.matrix([0.05,0.05,0.05]).T

r = np.matrix([1.0/3,1.0/3,1.0/3]).T

for i in range(1000):
	r = r_p(r)
print "Final PageRank: \n" + str(r)  
print "\n"

a = r[0]
b = r[1]
c = r[2]

print "0.95a = ", 0.95*a, "= 0.9c + 0.05b = ", 0.9*c + 0.05*b
print "0.95b = ", 0.95*b, "= 0.475a + 0.05c = ", 0.475*a + 0.05*c
print "0.95c = ", 0.95*c, "= 0.9b + 0.475a = ",  0.9*b + 0.475*a