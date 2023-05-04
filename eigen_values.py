import numpy as np

#Eigen Values

a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvectors)
print(eigenvalues)

b = eigenvectors[:, 0] * eigenvalues[0]
print(b)
