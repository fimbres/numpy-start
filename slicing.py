import numpy as np

#slicing

a = np.array([1, 2, 3, 4])
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
b = m[-1,-1]
print(b)

indexes = [0,2]
print(a[indexes])

even = np.argwhere(a%2==0).flatten()
print(even, a[even])
