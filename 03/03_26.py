import numpy as np 
a = np.array([(1, 2),(3,4)], dtype=[('a', np.int32), ('b', np.int32)])
print("Views")
print("a",a)
b = a.view(dtype=[('a', np.int16), ('b', np.int16)])
print("b",b)

