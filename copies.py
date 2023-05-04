import numpy as np

#copies

a = np.array([1,2,3])
b = a.copy()
b[0] = 10

print(a)
print(b)
