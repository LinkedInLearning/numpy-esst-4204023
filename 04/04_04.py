import numpy as np

# Zweidimensionales Array (2x3)
a2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Eindimensionales Array (1x3)
a1d = np.array([2, 3, 4])

r1 = np.add(a2d , a1d)
r2 = np.subtract(a2d , a1d)
r3 = np.multiply(a2d , a1d)
r4 = np.divide(a2d , a1d)
r5 = np.mod(a2d , a1d)
r6 = np.power(a2d , a1d)
r7 = np.sqrt(a2d)

print("Zweidimensionales Array:",a2d)
print("\nEindimensionales Array:", a1d)
print("\nErgebnis nach Addition:", r1)
print("\nErgebnis nach Subtraktion:", r2)
print("\nErgebnis nach Multiplikation:", r3)
print("\nErgebnis nach Division:", r4)
print("\nErgebnis nach Modulo:", r5)
print("\nErgebnis nach Potenzierung:", r6)
print("\nErgebnis nach Wurzelziehung:", r7)