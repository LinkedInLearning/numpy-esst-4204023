import numpy as np

matrix = np.array([[1, 2, 5, 9, 3],
                   [3, 4, 2, 8, 7]])

# Berechnen Sie den Index des Minimums und des Maximums
# bei beiden Achsen der Matrix

# Index des Minimums entlang der Zeilen
min_index_rows = np.argmin(matrix, axis=1)

# Index des Minimums entlang der Spalten
min_index_columns = np.argmin(matrix, axis=0)

# Index des Maximums entlang der Zeilen
max_index_rows = np.argmax(matrix, axis=1)

# Index des Maximums entlang der Spalten
max_index_columns = np.argmax(matrix, axis=0)

print("Index des Minimums entlang der Zeilen:", min_index_rows)
print("Index des Minimums entlang der Spalten:", min_index_columns)
print("Index des Maximums entlang der Zeilen:", max_index_rows)
print("Index des Maximums entlang der Spalten:", max_index_columns)