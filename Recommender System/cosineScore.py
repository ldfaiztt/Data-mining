import numpy as np
import math


def vectorLength(v):
    return math.sqrt(sum([vi**2 for vi in v]))

def vectorProducts(v1,v2):
    return np.dot(v1,v2)/(vectorLength(v1)*vectorLength(v2))

def cosineAngle(v, alpha):
	va = [vi for vi in v]
	va[-1] *= alpha
	return va

A = [1,0,1,0,1,2]
B = [1,1,0,0,1,6]
C = [0,1,0,1,0,2]

alphaVec = [0,0.5,1,2]

for alpha in alphaVec:
	
	AA = cosineAngle(A, alpha)
	AB = cosineAngle(B, alpha)
	AC = cosineAngle(C, alpha)	
	
	cosAB = vectorProducts(AA,AB)
	cosAC = vectorProducts(AA,AC)
	cosBC = vectorProducts(AB,AC)
	
	print "Alpha: %s" % alpha
	print "cos(A,B): %s" % (cosAB)
	print "cos(A,C): %s" % (cosAC)
	print "cos(B,C): %s" % (cosBC)
	print "\n",

#Alpha: 0
#cos(A,B): 0.666666666667
#cos(A,C): 0.0
#cos(B,C): 0.408248290464

#Alpha: 0.5
#cos(A,B): 0.721687836487
#cos(A,C): 0.288675134595
#cos(B,C): 0.666666666667

#Alpha: 1
#cos(A,B): 0.847318545736
#cos(A,C): 0.617213399848
#cos(B,C): 0.849836585599

#Alpha: 2
#cos(A,B): 0.946094540761
#cos(A,C): 0.865180912697
#cos(B,C): 0.952579344416