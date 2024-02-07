import numpy as np 
a = np.array([1,2,3,4,5,6,7])
# Nutzen Sie insert, um an der ersten Stelle des Arrays 42 hinzufügen
# Es wird ein neues Array erzeugt, das b zugewiesen wird.
b = np.insert(a,0,42)
# Geben Sie b aus.
print(b)
# Ändern Sie den Vektor mit 8 Elementen in eine Matrix (2, 4)
# Es wird ein neues Array erzeugt, das c zugewiesen wird.
c = b.reshape(2,4)
# Geben Sie c aus.
print(c)
# Nutzen Sie die Methode flatten, um aus c ein eindimensionales Array
# als Kopie zu erzeugen.
# Es wird ein neues Array erzeugt, das d zugewiesen wird.
d = c.flatten()
# Geben Sie d aus.
print(d)
# Ändern Sie den Wert des ersten Elements in d auf 0.
d[0] = 0
# Geben Sie c und d aus.
print("c",c)
print("d",d)
# Nutzen Sie die Methode ravel, um aus c ein eindimensionales Array
# als View zu erzeugen.
# Es wird ein neues Array erzeugt, das e zugewiesen wird.
e = c.ravel()
# Geben Sie e aus.
print(e)
# Ändern Sie den Wert des ersten Elements in e auf 0.
e[0] = 0
# Geben Sie c und e aus.
print("c",c)
print("e",e)