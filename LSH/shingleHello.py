str1 = "hello world"

def shingle(str):
	s = set()
	for i,c in enumerate(str):
		if i < len(str) - 2:
			shing = c+str[i+1]+str[i+2]
			print shing
			s.add(shing)
	print s
	return s

shingle1 = shingle(str1)
print('Number of 3-shinlges in "hello world" = '+str(len(shingle1)));