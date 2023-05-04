import numpy as np

#matrix operations

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m)
print(m.shape)
print(m[0][0])
print(m[0,0])
print(m[:,0])
print(m.T)
print(np.linalg.inv(m))
print(np.linalg.det(m))
print(np.diag(m))
