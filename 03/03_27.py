import numpy as np 
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Transponieren")
ta1 = np.transpose(a)
ta2 = a.T

print("Ursprüngliches Array:", a)
print("\nTransponiertes Array 1:", ta1)
print("\nTransponiertes Array 2:", ta2)
