import random

import numpy as np

matriz = np.array([
    [0, 1, 3, 3],
    [3, 4, 5, 3],
    [4, 5, 3, 0],
    [1, 7, 6, 2]
])
print(matriz.shape)
for x in range(4):
    for y in range(4):
        if y == 2:
            matriz[x] = random.randint(0, 100)
            matriz[y] = random.randint(0, 100)
            print("\t", matriz[x][y], end="\t")
        else:
            print("\t", matriz[x][y], end="\t")
    print("\n")


print("\n")
a = np.empty((2, 4), dtype=int)
for x in range(2):
    for y in range(4):
        a[x][y] = random.randint(1, 70)


for x in range(2):
    print("\t-" * 7)
    for y in range(4):
        if x == 2:
            print("\t", a[x][y], end="\t")
        else:
            print("\t", a[x][y], end="\t|")
    print("\n")
