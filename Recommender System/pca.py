import numpy as np

M = np.array([[1,1], [2,2], [3,4]])
MT = np.transpose(M)

MTM = np.dot(MT, M)

print "M: "
print M
print "MT: "
print MT
print "MTM: "
print MTM