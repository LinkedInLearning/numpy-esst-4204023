import numpy as np 
print("Zerlegen")
a =np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

# Array entlang der Zeilen aufteilen
sr = np.split(a, 3)

print("Aufgeteilte Arrays entlang der Zeilen:", sr)

# Array entlang der Spalten aufteilen
sc = np.split(a, 3, axis=1)

print("\nAufgeteilte Arrays entlang der Spalten:", sc)
