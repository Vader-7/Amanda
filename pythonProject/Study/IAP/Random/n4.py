filas = int(input("introduce el numero de filas: "))
columnas = int(input("introduce el numero de columnas: "))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input(f"fila {filas}, columnas {columnas} : ". format(i+1, j+1)))
        matriz[i].append(valor)

sumaFila=[sum(i) for i in matriz]
print (sumaFila)

sumarColumna=[sum(i) for i in zip(*matriz)]
print (sumarColumna)

print()
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print ("{}".format(elemento), end= " ")
    print("]")

print()