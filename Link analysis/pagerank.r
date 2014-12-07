# Q1 solution

# Start with:
# M =
#     [,A]  [,B]  [,C]
#[A,] 0.00  0.00  0.00
#[B,] 0.35  0.00  0.00
#[C,] 0.35  0.07  0.70

# r =
#          [,1]
#[1,] 0.3333333
#[2,] 0.3333333
#[3,] 0.3333333

# taxation
#     [,1]
#[1,]  0.1
#[2,]  0.1
#[3,]  0.1

# M, which is Beta (0.7) multiplied with transform matrix
# ie. M = matrix(c(0,0.5,0.5,0,0,1,0,0,1), nrow=3, ncol=3)
# Beta = 0.7
#to start with  M = M * Beta
M1 <- matrix(c(0, 7/20, 7/20, 0, 0, 7/10, 0, 0, 7/10), ncol = 3)
r1 <- matrix(c(1/3, 1/3, 1/3), ncol = 1)

# taxation = (1-Beta) = 0.3 multiplied by e ([1, 1, 1]) and divided by n = 3
taxation <- matrix(c(1/10, 1/10, 1/10), ncol = 1)
for (i in 1:1000) {
 r1 = (M1 %*% r1) + taxation
}
r1*3

#      [,1]
#[1,] 0.300
#[2,] 0.405
#[3,] 2.295

#####################################################

# Q2 solution

# Start with:
# M = 
#     [,A] [,B] [,C]
#[A,] 0.0  0.0  1.0
#[B,] 0.5  0.0  0.0
#[C,] 0.5  1.0  0.0

# Beta = 0.85

M2 <- matrix(c(0, 0.425, 0.425, 0, 0, 0.85, 0.85, 0, 0), ncol = 3)
r2 <- matrix(c(1/3, 1/3, 1/3), ncol = 1)

# taxation = (1-Beta) = 0.3 multiplied by e ([1, 1, 1]) and divided by n = 3
taxation <- matrix(c(0.05, 0.05, 0.05), ncol = 1)
for (i in 1:1000) {
    r2 = (M2 %*% r2) + taxation
}
r2

#          [,1]
#[1,] 0.3877897
#[2,] 0.2148106
#[3,] 0.3973997

0.95*r2[1]
0.9*r2[3] + 0.05*r2[2]
0.95*r2[2]
0.475*r2[1] + 0.05*r2[3]
0.95*r2[3]
0.9*r2[2] + 0.475*r2[1]

#######################################################

# Q3 solution
# There is no taxation ie. beta = 1

# Start with:
#     [,A] [,B] [,C]
#[A,] 0.0  0.0  1.0
#[B,] 0.5  0.0  0.0
#[C,] 0.5  1.0  0.0

#After 5 iterations
# transition matrix
M3 = cbind(c(0,0.5,0.5), c(0,0,1),  c(1,0,0))
# randomness parameter
beta = 1
# initialize ranks
r3 = rbind(1,1,1)
# power iteration after 5 iterations
for (i in 1:5) {
 r3 = beta * (M3 %*% r3) + (1-beta)/ncol(M3)
 print(r3)
}
# print ranks after 5th iteration
r3
#     [,1]
#[1,] 1.250
#[2,] 0.625
#[3,] 1.125

#At the limit (after 1000 iterations when r converges)
# transition matrix
M3 = cbind(c(0,0.5,0.5), c(0,0,1),  c(1,0,0))
# randomness parameter
beta = 1
# initialize ranks
r3 = rbind(1,1,1)
# power iteration after 1000 iterations
for (i in 1:1000) {
 r3 = beta * (M3 %*% r3) + (1-beta)/ncol(M3)
}
# print final ranks after 1000 iterations
r3
#     [,1]
#[1,] 1.2
#[2,] 0.6
#[3,] 1.2