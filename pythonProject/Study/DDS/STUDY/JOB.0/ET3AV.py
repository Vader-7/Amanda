# Variables
opcion = 0
indice = 0
contador = 1
pasajeros = []
# ET VUELOS
asientos = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
]


def menu():
    print("""
        1.- Ver disponibilidad
        2.- Comprar asiento
        3.- Anular pasaje
        4.- Modificar datos pasajero
        5.- SALIR
        """)


def diponibilidad():
    p_filas = 0
    p_indice = 0
    for p_asiento in asientos:
        if p_filas == 5:
            print("\t-\t" * 6)
            print("\t-\t" * 6)
        for p_a in p_asiento:
            if p_indice == 0:
                print("\t|", p_a, end=" ")
            elif p_indice == 5:
                print(" ", p_a, end="|")
            else:
                print("\t", p_a, end="\t")
            p_indice += 1
        p_filas += 1
        print("\n")
        p_indice = 0


def imprimePasajero():
    for v_pasajero in pasajeros:
        print(f"Rut:\t\t\t{v_pasajero[0]}")
        print(f"Nombre:\t\t\t{v_pasajero[1]}")
        print(f"Telefono:\t\t{v_pasajero[2]}")
        print(f"Banco:\t\t\t{v_pasajero[3]}")
        print(f"Asiento:\t\t{v_pasajero[4]}")


while opcion != 5:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("Ingresa un numero pls.")
    if opcion == 1:
        diponibilidad()
    elif opcion == 2:
        print("INGRESE LOS DATOS PARA COMPRAR SU ASIENTO.")
        print("Nombre:")
        nombre = input("...\t")
        print("RUT:")
        rut = input("...\t")
        print("Telefono:")
        telefono = input("...\t")
        print("Banco:")
        banco = input("...\t")
        pasajero = [rut, nombre, telefono, banco]
        diponibilidad()
        nro_asiento = int(input("\n-->\t"))
        for asiento in asientos:
            for a in asiento:
                if a == nro_asiento:
                    pasajero.append(a)
                    asiento[indice] = "XX"
                indice += 1
            indice = 0
        pasajeros.append(pasajero)
        pasajero = []
    elif opcion == 3:
        print("Ingrese su rut")
        rut = input("\n-->\t")
        for pasajero in pasajeros:
            # Segun Rut accedemos al asiento
            if rut in pasajero:
                for asiento in asientos:
                    for a in asiento:
                        # Si tiene un asiento asignado borra
                        if len(pasajero) > 4:
                            if pasajero[4] == contador:
                                asiento[indice] = pasajero[4]
                                pasajero.pop(4)
                        contador += 1
                        indice += 1
                    indice = 0
    elif opcion == 4:
        print("Ingrese su rut")
        rut = input("\n-->\t")
        print("Ingrese su asiento")
        asiento = int(input("\n-->\t"))
        for pasajero in pasajeros:
            if rut in pasajero:
                if asiento == pasajero[4]:
                    print("""
                            1 .- Nombre
                            2 .- Telefono
                            """)
                    opcion = int(input("\n-->\t"))
                    if opcion == 1 or opcion == 2:
                        print("Ingrese nueva información")
                        pasajero[opcion] = input("\n-->\t")
                    else:
                        print("Opción ingresada invalida.")
                        break
        imprimePasajero()
    elif opcion == 5:
        print("ADIOS.")
    else:
        print("Opción ingresada invalida.")
