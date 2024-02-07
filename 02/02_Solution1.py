import numpy as np 
rng = np.random.default_rng()
print("Simulation einer Ziehung der Lottozahlen.")
print("Es werden 6 zufällige Zahlen zwischen 1 und 49 (jeweils inklusive) ermittelt.")
print("Keine Zahl darf doppelt vorkommen.")
print("Das Ergebnis wird in einem NumPy-Array bereitgestellt.")

i = 0
s = set()
while len(s) < 6:
    s.add(rng.integers(1,50))
    i = i+1
lottozahlen = np.array(s)
print(lottozahlen)

