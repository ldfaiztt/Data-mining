# Author: Sheng Li
# Matrix:
#   C1  C2  C3  C4  C5  C6  C7
#   1   2   1   1   2   5   4
#   2   3   4   2   3   2   2
#   3   1   2   3   1   3   2
#   4   1   3   1   2   4   4
#   5   2   5   1   1   5   1
#   6   1   6   4   1   1   4

def candPair(x, y):
	i = 0
	while i < len(x):
		j = i + 1
		while j < len(x):
			if x[i] == x [j] and y[i] == y[j]:
				print "C%s,C%s" % (i+1,j+1)
			j += 1
		i += 1

candPair([1,2,1,1,2,5,4], [2,3,4,2,3,2,2])
candPair([3,1,2,3,1,3,2], [4,1,3,1,2,4,4])
candPair([5,2,5,1,1,5,1], [6,1,6,4,1,1,4])