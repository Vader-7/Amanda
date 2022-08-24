import os
import time


# Funciones
def menu():
    os.system("clear")
    print("""
        -   Menu reserva - 
    1.- Ver asientos disponibles.
    2.- Comprar asiento.
    3.- Anular vuelo.
    4.- Modificar datos pasajero.
    5.- Salir.
    """)


def validaDato(p_dato):
    while len(p_dato) < 2:
        print("Dato ingresado invalido.")
        p_dato = input("\n-->\t")
    return p_dato


# Variables
a_normal = 78000
a_vip = 240000
descuento = 0.15
opcion = 0
indice = 0
cont = 1
pasajeros = []
# Matriz
asientos = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
]


def disponibilidad():
    v_indice = 0
    v_filas = 0
    for v_asiento in asientos:
        if v_filas == 5:
            print("\t-" * 13)
            print("\t-" * 13)
        for v_a in v_asiento:
            if v_indice == 0:
                print("\t|\t", v_a, end="\t")
            elif v_indice == 5:
                print("\t", v_a, end="\t|\t")
            else:
                print("\t", v_a, end="\t")
            v_indice += 1
        print("\n")
        v_indice = 0
        v_filas += 1


while opcion != 5:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("Ingrese una opción valida.")
        time.sleep(3)
    if opcion == 1:
        print("Disponibilidad de asientos.")
        disponibilidad()
        time.sleep(3)
    elif opcion == 2:
        nombre = validaDato(input("\n-->\t"))
        rut = validaDato(input("\n-->\t"))
        telefono = validaDato(input("\n-->\t"))
        banco = validaDato(input("\n-->\t"))
        pasajero = [nombre, rut, telefono, banco]
        print("Ingrese el nro de asiento.")
        nro_asiento = int(input("\n-->\t"))
        disponibilidad()
        for asiento in asientos:
            for a in asiento:
                if a == nro_asiento:
                    pasajero.append(a)
                    asiento[indice] = "x"
                else:
                    indice += 1
            indice = 0
        pasajeros.append(pasajero)
        pasajero = []
    elif opcion == 3:
        print("Ingrese su rut.")
        rut = input("\n-->\t")
        for pasajero in pasajeros:
            for p in pasajero:
                if rut in p:
                    print(f"Nombre:\t\t{pasajero[0]}")
                    print(f"RUT:\t\t{pasajero[1]}")
                    print(f"Telefono:\t\t{pasajero[2]}")
                    print(f"Banco:\t\t{pasajero[3]}")
                    print(f"Pasaje:\t\t{pasajero[4]}")
                    for asiento in asientos:
                        for a in asiento:
                            if asiento[4] == cont:
                                asiento[indice] = pasajero[4]
                            cont += 1
                            indice += 1
                        indice = 0

    elif opcion == 4:
        print("Ingrese su rut.")
        rut = input("\n-->\t")
    elif opcion == 5:
        pass
    else:
        print("Opción ingresada invalida.")
        time.sleep(3)
