import numpy as np 
print("Iterieren")
a = np.arange(0,30)
for e in np.nditer(a):
    print(e)