import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])

print("Array:", a, a.dtype)
a[0] = 4.12
print("Array:", a, a.dtype)
a = np.array(a,dtype=float)
print("Array:", a, a.dtype)
a[0] = 4.12
print("Array:", a, a.dtype)

