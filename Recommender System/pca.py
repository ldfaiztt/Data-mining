import numpy as np

M = np.array([[1,1], [2,2], [3,4]])
MT = np.transpose(M)

MTM = np.dot(MT, M)

print "M: "
print M

#M: 
#[[1 1]
# [2 2]
# [3 4]]


print "MT: "
print MT

#MT: 
#[[1 2 3]
# [1 2 4]]

print "MTM: "
print MTM

#MTM: 
#[[14 17]
# [17 21]]