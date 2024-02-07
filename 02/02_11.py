import numpy as np 
a1 = np.array([1, 2, 3, 4, 5, 6] )
a2 = np.array([[1, 2, 3], [4, 5, 6]] )
a3 = np.array([[1, 2],[ 3, 4], [5, 6]] )
a4 = np.array([[[1, 2],[ 3, 4]],[[5, 6],[ 7, 8]],[[9, 10],[ 11, 12]]] )
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)