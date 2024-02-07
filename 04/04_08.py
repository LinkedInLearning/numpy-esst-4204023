import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])

np.save('numpy_array', a)
b = np.load('numpy_array.npy')
print(b)

np.savetxt('numpy_array.csv', a)
c = np.loadtxt('numpy_array.csv')
print(c)
