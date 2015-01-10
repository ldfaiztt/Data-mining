# Author: Sheng Li

# LSH family h (d1, d2, p1, p2) = (d1, d2, 0.6, 0.4)
p1 = 0.6
p2 = 0.4

# We can use three functions from h and the AND-construction to form a (d1,d2,w,x) family
# we cube the probabilities associated with h
# (d1, d2, (p1)^3, (p2)^3)
def AND_hash(p):
	return p ** 3

# We can use two functions from h and the OR-construction to form a (d1,d2,y,z) family
# we take each probability associated with h, subtract it from 1, 
# square the result, and subtract that from 1
def OR_hash(p):
	return 1 - (1-p) ** 2


print "w: ", AND_hash(p1)
print "x: ", AND_hash(p2)
print "y: ", OR_hash(p1)
print "z: ", OR_hash(p2)

#w:  0.216
#x:  0.064
#y:  0.84
#z:  0.64