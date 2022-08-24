import numpy as np

# Variables
opcion = 0
indice = 0

asientos = np.arange(1, 43, 1).reshape(7, 6)
asientos = asientos.astype(str)
print(asientos)


def menu():
    print("""
        - MENU -
        1.- Ver disponibilidad de asientos
        2.- Comprar asiento
        3.- Anular vuelo
        4.- Modificar datos de pasajero
        5.- Salir
    """)


menu()

for x in range(7):
    indice = 0
    for y in range(6):
        if indice == 2:
            print(asientos[x][y], end="\t")
        else:
            print(asientos[x][y], end="")
        indice += 1
    print("\n")


"""asiento = input("\n-->\t")
for a in range(7):
    for b in range(6):
        if asientos[a][b] == asiento:
            print("Asiento disponible.")
            asientos[a][b] = "x"""

# while opcion != 4
