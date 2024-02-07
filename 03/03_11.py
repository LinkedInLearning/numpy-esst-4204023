import numpy as np 
a = np.arange(0,30)
print("a",a, a.shape)
a.shape=[2,15]
print("a",a, a.shape)
b = a.copy()
print("b",b, b.shape)
b.shape=[30,]
print("b",b, b.shape)
c = b.copy()
print("c",c, c.shape)
c.shape=[10,3]
print("c",c, c.shape)
