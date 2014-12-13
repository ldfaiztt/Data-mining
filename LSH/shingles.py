#Author: Sheng Li

str1 = "ABRACADABRA"
str2 = "BRICABRAC"

def getShingles(str):
    shingles = []
    doc_shingles = []
    for i in range(len(str)-1):
        shingles.append(str[i]+str[i+1])
    return set(shingles)
        
def getCommon(list1,list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2))

def getTotal(list1,list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.union(s2))

print "Set of 2-shinlges in ABRACADABRA =",  getShingles(str1)
print "Set of 2-shinlges in BRICABRAC =", getShingles(str2)

print "Number of 2-shinlges in ABRACADABRA = ", len(getShingles(str1))
print "Number of 2-shinlges in BRICABRAC = ", len(getShingles(str2))

print "Number of Common Shingles = ", getCommon(getShingles(str1),getShingles(str2))
print "Total Number of Shingles = ", getTotal(getShingles(str1),getShingles(str2))
