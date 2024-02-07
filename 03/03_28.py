import numpy as np 
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Umdrehen")
print(a)

# Umdrehen der Reihen entlang der ersten Achse (vertikal umdrehen)
fa1 = np.flip(a, axis=0)

# Umdrehen der Spalten entlang der zweiten Achse (horizontal umdrehen)
fa2 = np.flip(a, axis=1)

# Umdrehen ohne Achsen
fa3 = np.flip(a)


print("Ursprüngliches Array:", a)
print("\nVertikal umgedrehtes Array:", fa1)
print("\nHorizontal umgedrehtes Array:", fa2)
print("\nKomplett umgedrehtes Array:", fa3)

