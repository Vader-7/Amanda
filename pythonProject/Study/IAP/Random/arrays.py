import numpy

"""v_arreglo = numpy.array([1, 5, 7])
for i in range(len(v_arreglo)):
    print(v_arreglo[i])"""

largo = int(input("Ingrese el tamaño de su arreglo: "))
nombres = numpy.array([None] * largo)
for i in range(len(nombres)):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres[i] = nombre
for i in range(len(nombres)):
    print(nombres[i])
