# Variables
opcion = 0
indice = 0
cont = 1
valor_normal = 78000
valor_vip = 2400000
descuento = 0.15
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


def validaDato(p_dato):
    while len(p_dato) < 2 or " " in p_dato:
        print("Dato ingresado invalido, reingrese.")
        p_dato = input("\n-->\t")
    return p_dato


def imprimePasajero():
    for v_pasajero in pasajeros:
        print(f"Nombre:\t\t\t{v_pasajero[0]}")
        print(f"Rut:\t\t\t{v_pasajero[1]}")
        print(f"Telefono:\t\t{v_pasajero[2]}")
        print(f"Banco:\t\t\t{v_pasajero[3]}")
        print(f"Valor pasaje:\t{round(v_pasajero[4])}")
        print(f"Asiento:\t\t{v_pasajero[5]}")


# función disponibilidad
def asientodisponible():
    v_indice = 0
    v_fila = 0
    for v_asiento in asientos:
        if v_fila == 5:
            print("\t-\t" * 7)
            print("\t-\t" * 7)
        for v_a in v_asiento:
            if v_indice == 0:
                print("\t|\t", v_a, end="\t")
            elif v_indice == 5:
                print("\t", v_a, end="\t|")
            else:
                print("\t", v_a, end="\t")
            v_indice += 1
        print("\n")
        v_fila += 1
        v_indice = 0


# función menu
def menu():
    print("""
        1.- Ver asientos disponibles
        2.- Comprar asiento
        3.- Anular vuelo
        4.- Modificar pasaje
        5.- Salir
    """)


while opcion != 5:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("Opción ingresada invalida.")
    if opcion == 1:
        asientodisponible()
    elif opcion == 2:
        print("-Datos usuario-")
        print("Nombre")
        nombre = validaDato(input("\n-->\t"))
        print("Rut")
        rut = validaDato(input("\n-->\t"))
        print("Telefono")
        telefono = validaDato(input("\n-->\t"))
        print("Banco")
        banco = validaDato(input("\n-->\t"))
        pasajero = [rut, nombre, telefono, banco]
        asientodisponible()
        nro_asiento = int(input("\n-->\t"))
        if nro_asiento > 30:
            valor_pasaje = valor_vip
            descuento = valor_pasaje * descuento
            valor_pasaje = valor_pasaje - descuento
        else:
            valor_pasaje = valor_normal
            descuento = valor_pasaje * descuento
            valor_pasaje = valor_pasaje - descuento
        pasajero.append(valor_pasaje)
        for asiento in asientos:
            for a in asiento:
                if nro_asiento == a:
                    asiento[indice] = "x"
                    pasajero.append(nro_asiento)
                    # pasajero.append(valor_vip)
                indice += 1
            indice = 0
        pasajeros.append(pasajero)
        pasajero = []
        imprimePasajero()
    elif opcion == 3:
        print("Ingrese su rut")
        rut = input("\n-->\t")
        for pasajero in pasajeros:
            # Segun Rut accedemos al asiento
            if rut in pasajero:
                for asiento in asientos:
                    for a in asiento:
                        if pasajero[5] == cont:
                            asiento[indice] = pasajero[5]
                        cont += 1
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
                    if opcion == 2 or opcion == 0:
                        print("Ingrese nueva información")
                        pasajero[opcion] = input("\n-->\t")
                    else:
                        print("Opción ingresada invalida.")
                        break
        imprimePasajero()
