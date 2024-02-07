import numpy as np 
print("Zerlegen")
a = np.arange(0,30)
# Indizes der geraden und ungeraden Zahlen extrahieren
even_indices = np.where(a % 2 == 0)
odd_indices = np.where(a % 2 != 0)

# Array in zwei Teile aufteilen basierend auf den Indizes
gerade_zahlen = a[even_indices]
ungerade_zahlen = a[odd_indices]

print("Gerade Zahlen:", gerade_zahlen)
print("\nUngerade Zahlen:", ungerade_zahlen)