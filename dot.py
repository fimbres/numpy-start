import numpy as np

#dot operation
##### python lists #####

l1 = [1, 2, 3]
l2 = [4, 5, 6]

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]

print(dot)

##### numpy ######

a1 = np.array(l1)
a2 = np.array(l2)

dot = np.dot(a1, a2)
print(dot)
