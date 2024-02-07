import numpy as np

# Ein 3D-Array erstellen
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Das gesamte Array anzeigen
print("3D-Array:")
print(a[0])
print(a[1])
# Zugriff auf einzelne Elemente
e1 = a[0, 1, 2]  # Wert in der ersten Ebene, zweiten Zeile, dritten Spalte
e2 = a[1, 0, 1]  # Wert in der zweiten Ebene, ersten Zeile, zweiten Spalte
e3 = a[0] [1] [2] 
print("\nZugriff auf einzelne Elemente:")
print("Element 1:", e1)
print("Element 2:", e2)
print("Element 2:", e3)