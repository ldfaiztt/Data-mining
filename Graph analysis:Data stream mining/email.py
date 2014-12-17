# Author: Sheng Li

def email(n):
	t = (10**14)/n-1
	return t

print "t-value when n=10^9: ", email(10**9)
print "t-value when n=10^10: ", email(10**10)
print "t-value when n=10^11: ", email(10**11)
print "t-value when n=10^12: ", email(10**12)
print "t-value when n=10^13: ", email(10**13)
print "t-value when n=10^14: ", email(10**14)
