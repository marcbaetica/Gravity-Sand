import numpy as np
from random import randint


a = np.zeros((10, 10))

for _ in range(20):
    a[randint(0, 9)][randint(0, 9)] = 2
a[5][5] = 1

print(a)

