import numpy as np 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.stack((a, b))
print(c)
d = np.stack((a, b), axis=1)
print(d)