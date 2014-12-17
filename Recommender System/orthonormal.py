# Author: Sheng Li
# Identify [x,y,z] that is orthonormal to [2/7,3/7,6/7] and 
# x^2 + y^2 + z^2 = 1

import numpy as NP

M = NP.array([[0.702, -0.702, 0.117],
              [-0.548, 0.401, 0.273],
              [-0.288, -0.490, 0.772],
              [0.975, 0.700, -0.675]])


V1 = (0.702)**2 + (-0.702)**2 + (0.117)**2
print V1

V2 = (-0.548)**2 + (0.401)**2 + (0.273)**2
print V2

V3 = (-0.288)**2 + (-0.490)**2 + (0.772)**2
print V3

V4 = (0.975)**2 + (0.700)**2 + (-0.675)**2
print V4


Y = NP.transpose(NP.array([2, 3, 6]))
A = NP.dot(M, Y)
print A


