import numpy as np

#importing data

data = np.loadtxt('./data/financial-report.csv', delimiter=",", dtype=np.str_, usecols=13)

print(data)
