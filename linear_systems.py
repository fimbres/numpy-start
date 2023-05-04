import numpy as np

#solving linear systems

#x1 + x2 = 2200
#1.5x1 + 4x2 = 5050

A = np.array([[1, 1], [1.5, 4]])
B = np.array([2200, 5050])

X = np.linalg.solve(A, B)

print(X)
