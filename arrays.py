import numpy as np

a = np.array([1, 2, 3, 4])

# printing array properties

print(a)
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.itemsize)

#modify items

print(a[0])
a[0] = 10
print(a[0])

#array vs list

l = [1, 2, 3]
print(l * 2)
print(a * 2)
l.append(4)
# a.append(4) -> this will crash!
print(l + [4])
print(a + np.array([4]))

#fill arrays

b = np.zeros((2, 3))
c = np.ones((2, 3))
d = np.full((2, 3), 5.0)
e = np.eye(3)
e = np.linspace(0, 10, 5)

print(b, c, d, e)
