import numpy as np 
a = np.arange(30)

b = a.reshape((2, -1, 3))  # -1 steht für "was notwendig ist"
c = a.reshape((15, -1))  # -1 steht für "was notwendig ist"
d = a.reshape((10, -1))  # -1 steht für "was notwendig ist"
print(b,b.shape)
print(c,c.shape)
print(d,d.shape)