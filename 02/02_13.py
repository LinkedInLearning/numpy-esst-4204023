import numpy as np 
rng = np.random.default_rng()
zz = rng.random()
print(zz)
za1 = rng.standard_normal(5)
print(za1)
za2 = rng.integers(low=5, high=42,size=10)
print(za2)
a3 = np.arange(1,42,3)
print(a3)
rng.shuffle(a3)
print(a3)