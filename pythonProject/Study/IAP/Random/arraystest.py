import numpy

n = numpy.array([
    [["amarillo", "rojo", "naranja"], ["azul", "blanco", "rojo"], ["azul", "blanco", "rojo"]],
    [["azul", "blanco", "rojo"], ["azul", "blanco", "rojo"], ["azul", "blanco", "rojo"]],
    [["blanco", "azul", "amarillo"], ["azul", "blanco", "rojo"], ["azul", "blanco", "rojo"]]])
print(n.shape)
contAmarillo = 0
contBlanco = 0
contAzul = 0
contRojo = 0
contNaranja = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if n[i][j][k] == "blanco":
                contBlanco = contBlanco + 1
            if n[i][j][k] == "azul":
                contAzul = contAzul + 1
            if n[i][j][k] == "naranja":
                contNaranja = contNaranja + 1
            if n[i][j][k] == "rojo":
                contRojo = contRojo + 1
            if n[i][j][k] == "amarillo":
                contAmarillo = contAmarillo + 1
print(f"Número de veces que el color Azul se encuentra en la matriz es: {contAzul}")
print(f"Número de veces que el color Rojo se encuentra en la matriz es: {contRojo}")
print(f"Número de veces que el color Blanco se encuentra en la matriz es: {contBlanco}")
print(f"Número de veces que el color Naranja se encuentra en la matriz es: {contNaranja}")
print(f"Número de veces que el color Amarillo se encuentra en la matriz es: {contAmarillo}")

matriz = numpy.array([
    [3, 10, 4, 16],
    [1, 7, 8, -7],
    [9, -1, 3, 9]
])
for i in range(3):
    for k in range(4):
        print(matriz[i][k], end="")
        print("\t", end="")
    print("")
"""asientos = int(input("Ingrese numero de asientos: "))
filas = int(input("Ingrese numero de filas: "))
bus = numpy.array([[None] * asientos, [None] * filas])
print(bus.shape)"""
