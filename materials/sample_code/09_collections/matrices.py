matrix1 = [[0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0],
           [0, 2, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 3, 0]]

matrix2 = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(matrix1[0][3])    # the nested list way: two integer indexing
print(matrix2[(0, 3)])  # the tuple way: one tuple indexing

print(matrix2.get((0, 3)))
print(matrix2.get((1, 3), 0))