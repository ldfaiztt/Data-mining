# Author: Sheng Li

import numpy as np

# The 8 strings that represent sets:
s1 = "abcef"
s2 = "acdeg"
s3 = "bcdefg"
s4 = "adfg"
s5 = "bcdfgh"
s6 = "bceg"
s7 = "cdfg"
s8 = "abcd"

# Upper limit on Jaccard distance is 0.2
# We index a string of length L on the symbols appearing in its prefix of length floor(0.2L+1)
# Strings of length 5 and 6 are indexed on their first 2 symbols
# Strings of length 4 are indexed on their first symbol
Jaccard = 0.2

def prefxlen(str, Jaccard):
	return int(np.floor(len(str)*Jaccard + 1))

s = [s1, s2, s3, s4, s5, s6, s7, s8]
length = map(lambda s: prefxlen(s, Jaccard), s)
print "Prefix lenth of s1 to s8:", length
print " "
#Prefix length of s1 to s8: [2, 2, 2, 1, 2, 1, 1, 1]

# We want to find the strings in index a, b and c
def index(str):
	indx = {}
	for s in str:
		for l in range(prefxlen(s, Jaccard)):
			if s[l] in indx:
				indx[s[l]].append(s)
			else:
				indx[s[l]] = [s]   
	return indx
    
indx = index(s)
print "strings in a, b and c:", indx
print " "
#strings in a, b and c: {'a': ['abcef', 'acdeg', 'adfg', 'abcd'], 'c': ['acdeg', 'bcdefg', 'bcdfgh', 'cdfg'], 'b': ['abcef', 'bcdefg', 'bcdfgh', 'bceg']}

# Number of strings compared with each of s1, s3 and s6 when it is used as the probe string
def count(indx, s):
	counts = set(sum([indx[s[l]] for l in range(prefxlen(s, Jaccard))], []))
	counts.remove(s)
	return (s, len(counts), counts)

print "String, number of strings for comparisons, set of strings for comparisons:" 
for s in [s1, s3, s6]:
	print count(indx, s)
#String, number of strings for comparisons, set of strings for comparisons:
#('abcef', 6, set(['abcd', 'bcdfgh', 'acdeg', 'adfg', 'bceg', 'bcdefg']))
#('bcdefg', 5, set(['cdfg', 'abcef', 'bcdfgh', 'acdeg', 'bceg']))
#('bceg', 3, set(['bcdfgh', 'abcef', 'bcdefg']))