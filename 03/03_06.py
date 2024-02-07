import numpy as np 
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("a",a)
b = np.delete(a,1)
print("b",b)
c = np.delete(a,1, axis=1)
print("c",c)
