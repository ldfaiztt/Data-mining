#Author: Sheng Li

from collections import defaultdict
from itertools import combinations

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

strings = ["he","she","his","hers"]
pairs =  list(combinations(strings,2))

length = defaultdict(list)
for pair in pairs:
    x = pair[0]
    y = pair[1]
    dist = len(x) + len(y) - 2 * (len(lcs(x,y)))
    length[dist].append((x,y))


for k,v in length.items():
    print k,v