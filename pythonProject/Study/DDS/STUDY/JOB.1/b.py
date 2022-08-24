def datos(p_cantidad):
    lista = []
    for i in range(p_cantidad):
        print(f"Ingrese el {i + 1} dato.")
        p_dato = input("\n-->\t")
        lista.append(p_dato)
    return lista


def informe(p_lista):
    print("\tInforme.")
    for dato in p_lista:
        print(f"\t-\t{dato}")


print("Ingrese la cantidad de invitados.")
cantidad = int(input("\n-->\t"))
datos = datos(cantidad)
informe(datos)