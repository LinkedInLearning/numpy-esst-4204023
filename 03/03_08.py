import numpy as np 
a = np.array([[4,1],[3,2],[5,1]])
print("a",a)
b = np.sort(a)
print("b",b)
c = np.sort(a, axis=0)
print("c",c)
d = np.sort(a, axis=1)
print("d",d)