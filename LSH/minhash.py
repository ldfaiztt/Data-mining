import numpy as np

def convertToRows(minhash_row, order):
    the_rows = []

    for item in minhash_row:
        the_rows.append(order[item - 1])

    return the_rows


def minhash(matrix, order):
    m = matrix.shape[1]
    minhash_row = [0] * m
    i = 1

    for r in order:
        row = matrix[r - 1]
        for c in range(0, m):
            if minhash_row[c] == 0:
                minhash_row[c] = i * row[c]
        i += 1
        if 0 not in minhash_row:
            break

    return minhash_row

matrix = np.array([[0, 1, 1, 0],
                   [1, 0, 1, 1],
                   [0, 1, 0, 1],
                   [0, 0, 1, 0],
                   [1, 0, 1, 0],
                   [0, 1, 0, 0]])
order = [4, 6, 1, 3, 5, 2]
minhash_row = minhash(matrix, order)
rows_that_contributed = convertToRows(minhash_row, order)
print(rows_that_contributed)