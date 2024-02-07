import numpy as np

# Zweidimensionales Array (2x3)
a2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Eindimensionales Array (1x3)
a1d = np.array([2, 3, 4])

# Broadcasting und Multiplikation durchführen
result = np.add(a2d * a1d)

print("Zweidimensionales Array:",a2d)
print("\nEindimensionales Array:", a1d)
print("\nErgebnis nach der Multiplikation mit Broadcasting:", result)