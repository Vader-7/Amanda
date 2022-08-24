opcion = 0


def menu():
    print("""
    1.- Saludar.
    2.- Salidar con Nombre.
    3.- Sumar (retorno).
    4.- Convertir a metros.
    """)


def opcionM(p_opcion):
    if p_opcion == 1:
        pass
    elif p_opcion == 2:
        pass
    elif p_opcion == 3:
        pass
    elif p_opcion == 4:
        pass
    elif p_opcion == 5:
        print("Adios.")
    else:
        print("Opción no valida.")


while opcion != 5:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("Opción no valida.")
    opcionM(opcion)
