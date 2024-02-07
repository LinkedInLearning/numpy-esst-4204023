import numpy as np

# Erstelle ein 2D-Array
a = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Definiere Indizes für Zeilen und Spalten
rows = [0, 2]
columns = [1, 2]

# Verwende ix_(), um Indizes zu generieren
i = np.ix_(rows, columns)

# Gib die generierten Indizes aus
print("Generierte Indizes:", i)

# Verwende die generierten Indizes, um auf bestimmte Elemente des Arrays zuzugreifen
elemente = a[i]

# Gib die ausgewählten Elemente aus
print("Ausgewählte Elemente des Arrays:", elemente)
