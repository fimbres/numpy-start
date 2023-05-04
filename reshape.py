import numpy as np

#reshape

a = np.array([1, 2, 3, 4])
print(a.shape)
print(a)

b = a.reshape(2,2)
print(b.shape)
print(b)
print(np.arange(1,7))

na = np.newaxis
c = b[:, na]
print(c.shape, na)
