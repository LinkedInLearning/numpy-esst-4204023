import numpy as np
a = np.array([[1, 2, 3],
                [4, 5, 6]])

# Summe über die Spalten (axis=0)
sum_spalten = np.sum(a, axis=0)

# Summe über die Zeilen (axis=1)
sum_zeilen = np.sum(a, axis=1)

sum_gesamt  = np.sum(a)

print("Array:", a)
print("Summe über die Spalten:", sum_spalten)
print("Summe über die Zeilen:", sum_zeilen)
print("Summe gesamt:", sum_gesamt)