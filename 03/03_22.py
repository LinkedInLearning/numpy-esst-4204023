import numpy as np 
print("Iterieren")
a = np.arange(0,30).reshape(15,2)
for e in a:
    print(e)
for e in a.T:
    print(e)
for e1 in a:
    print(e1)
    for e2 in e1:
      print(e2)
