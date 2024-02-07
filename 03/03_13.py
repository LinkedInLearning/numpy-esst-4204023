import numpy as np 
a = np.arange(0,30)
print("a",a, a.shape)
b=np.reshape(a,newshape=(2,15))
print("a",a, a.shape)
print("b",b, b.shape)
cv = a[:,np.newaxis]
print("cv",cv)
rv = a[np.newaxis,:]
print("rv",rv)
