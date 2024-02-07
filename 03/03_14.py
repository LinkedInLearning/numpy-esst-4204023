import numpy as np 
print("Indizieren")
a = np.arange(-10,30)

print(a[6:8])
print(a[6:-1])
print(a[-8])
print(a[a <= 5])
print(a[a % 3 == 0])
print(a[(a > 2) & (a < 11)])

b = a.copy().reshape(20,2)
print(b[6:8])
c = np.nonzero(a)
print(c)
d = np.nonzero(a > -2)
print(d)