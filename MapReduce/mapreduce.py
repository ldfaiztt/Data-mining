from collections import defaultdict
import math

# determine if an integer n is a prime number
def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

# Output the prime divisors of each integers
reduce = defaultdict(list)
def map(integer):
	output = []
	for i in range(2, integer):
		if isPrime(i) and integer%i == 0:
			output.append(i)
	return output

# Input list of integers
integer = [15, 21, 24, 30, 49]

# Print every integer and its prime divisor(s)
# eg. The prime divisors of 15 are 3 & 5
for n in integer:
    print "Integer:", n
    primeDivisor = map(n)
    print "Prime divisor(s):", primeDivisor
    for key in primeDivisor:
        reduce[key].append(n)
 
#print reduce.items()

# Output every prime divisor and the sum of its corresponding integers
print "\n"
for key, values in reduce.items():
    print "prime divisor and the sum of integers:", key, ",", sum(values)