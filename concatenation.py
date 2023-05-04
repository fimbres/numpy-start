import numpy as np

#concatination

a = np.array([1, 2, 3, 4])
print(a)

m = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9]])
c = np.concatenate((m,b))
print(c)

# hstack - returns an array, vstack - returns a matrix
b = np.array([7, 8, 9, 10])
h = np.hstack((a, b))
v = np.vstack((a, b))
print(h, v)