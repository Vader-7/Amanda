import numpy as np
from random import randint

"""
lista = [10, 20, 30, 70]
print(lista)
arreglo = np.array(lista)

print(arreglo)
print(arreglo.ndim)
print(len(arreglo))
print(arreglo.shape)
print(arreglo.size)
print(arreglo.max())
print(arreglo.min())
print(arreglo.mean())
print(arreglo[1:3])
print(arreglo.sum())
"""
lista = []
print("Ingrese el tamaño del arreglo")
tam = int(input("-->"))
for i in range(tam):
    lista.append(randint(0, 100))

arreglo = np.array(lista)
print(arreglo)
