import numpy as np

#funcions

f = np.array([[7, 8, 9, 10, 11, 12, 13], [17, 18, 19, 20, 21, 22, 23]])
    
print(f)
print(f.sum(axis=1))
print(f.mean())
print(np.std(f))
print(np.max(f))
print(np.min(f))
