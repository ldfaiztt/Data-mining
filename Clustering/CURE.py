# Author: Sheng Li
# representative set of points: x = (0,0); y = (10,10) 
# a = (1,6); b = (3,7); c = (4,3); d = (7,7), e = (8,2); f = (9,5)
# selection order: e, b, c, d, f, a

import math

# Function to calculate Euclidean distance:
def calcDistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Representative set of points:
rep = [(0,0),(10,10)]
left = [(1,6), (3,7), (4,3), (7,7), (8,2), (9,5)]

# Find the next representative points in the set of points in left
while len(left) > 0:		
	maxD = -1
	maxP = None
	for p in left:
		curD = min([calcDistance(p, sp) for sp in rep])
		if curD > maxD:
			maxD = curD
			maxP = p
	rep.append(maxP)
	left.remove(maxP)

print rep