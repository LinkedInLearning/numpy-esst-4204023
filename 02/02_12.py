import numpy as np 
a1 = np.array([1, 2, 3, 4, 5, 6] )
a2 = np.array([1, 2, 3, 4.0, 5, 6] )
a3 = np.array([[1, 2],[ 3, 4], [5, 6]] )
a4 = np.array([[[1, 2],[ 3, 4]],[[5, 6],[ 7, 8]],[[9, 10],[ 11, 12]]] )
print(a1, "\nAnzahl Elemente mit size", a1.size )
print("\nAnzahl Elemente mit prod und shape", np.prod(a1.shape), "\n",10*"-")

print(a2, "\nAnzahl Elemente",a2.size, "\n",10*"-")
print(a3, "\nAnzahl Elemente",a3.size, "\n",10*"-")
print(a4, "\nAnzahl Elemente",a4.size, "\n",20*"-")
print(a1, "\nGroesse Elemente in Byte", a1.itemsize, "\n",10*"-")
print(a2, "\nGroesse Elemente in Byte",a2.itemsize, "\n",20*"-")
print(a1, "\nDatentyp Elemente", a1.dtype, "\n",10*"-")
print(a2, "\nDatentyp Elemente",a2.dtype, "\n",10*"-")