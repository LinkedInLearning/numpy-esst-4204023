import numpy as np 
a = np.array([1,2,3,4,5,6])
print("Flache Kopie")
print("a",a)
b = a
print("b",b)
a[0] = 10
print("a",a)
print("b",b)
b[0] = 42
print("a",a)
print("b",b)
