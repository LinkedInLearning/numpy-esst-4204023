import numpy as np 
print("Iterieren")
a = np.arange(0,30).reshape(15,2)
for e in np.nditer(a):
    print(e)
print(a, a.shape)
