import numpy as np 
rng = np.random.default_rng()
print("Simulation einer Ziehung der Lottozahlen.")
print("Es werden 6 zufällige Zahlen zwischen 1 und 49 (jeweils inklusive) ermittelt.")
print("Keine Zahl darf doppelt vorkommen.")
print("Das Ergebnis wird in einem NumPy-Array bereitgestellt.")
za = np.arange(1,50)
rng.shuffle(za)
i = 0
l = []
while i < 6:
    l.append(za[i])
    i = i+1
lottozahlen = np.array(l)
print(lottozahlen)

