import numpy as np
a = np.array([6, 2, 3, 14, 5, 9])
b = np.array([2, 3, 4, 5, 26, 8])

r1 = np.max(a)
r2 = a.max()
r3 = np.min(a)
r4 = np.prod(a)
r5 = np.average(a)
r6 = np.mean(a)

print("Array:",a)
print("Maximum:", r1)
print("Maximum:", r2)
print("Minimum:", r3)
print("Produkt:", r4)
print("Durchschnitt:", r5)
print("Mittelwert:", r6)