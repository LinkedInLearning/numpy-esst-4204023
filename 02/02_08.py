import numpy as np 
a1 = np.eye(3,5)
#print(a1)
a2 = np.diag([1, 2, 3, 4])
#print(a2)
a3 = np.array([1, 2, 3, 4])

# Standardmäßig (increasing=False) erstellt die Funktion eine absteigende Vandermonde-Matrix
vmd = np.vander(a3)
print("Absteigende Vandermonde-Matrix:\n", vmd)

# Mit increasing=True erstellt die Funktion eine aufsteigende Vandermonde-Matrix
vma = np.vander(a3, increasing=True)
print("\nAufsteigende Vandermonde-Matrix:\n", vma)