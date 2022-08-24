opcion = 0
adm_opcion = 0
productos = []
p = []


def menu():
    print("""
        -- Registro productos.
        1.- Registrar producto.
        2.- Lista productos.
        3.- Administracón.
        4.- Vender.
        5.- Salir.
    """)


def menuAdmin():
    print("""
        -- Administracón.
        1.- Eliminar producto.
        2.- Modificar producto.
        3.- Revisar producto mas vendido.
        4.- Volver Menu.
    """)


def informeProducto():
    for p in productos:
        print(f"\t-PRODUCTO ID:\t{p[0]}")
        print(f"\t-NOMBRE:\t{p[1]}")
        print(f"\t-PRECIO:\t{p[2]}")
        print(f"\t-CANTIDAD:\t{p[3]}")
        print(f"\t-NRO DE VENTAS:\t{p[4]}")
        print("\n")


def validaCampo(p_campo):
    while len(p_campo) < 2 or " " in p_campo:
        print("Dato ingresado invalido, reingrese.")
        p_campo = input("-->")
    return p_campo


while opcion != 5:
    menu()
    try:
        opcion = int(input("-->"))
    except ValueError:
        print("No ingrese letras pls.")
    if opcion == 1:
        print("Ingrese ID producto.")
        while True:
            try:
                id = int(input("\n-->\t"))
                break
            except ValueError:
                print("ID ingresado invalido.")
        print("Ingrese nombre producto.")
        nombre = validaCampo(input("-->"))
        print("Ingrese precio producto.")
        while True:
            try:
                precio = int(input("\n-->\t"))
                break
            except ValueError:
                print("Precio ingresado invalido.")
        print("Ingrese stock producto.")
        while True:
            try:
                stock = int(input("\n-->\t"))
                break
            except ValueError:
                print("Stock ingresado invalido.")
        nro_ventas = 0
        producto = [id, nombre, precio, stock, nro_ventas]
        productos.append(producto)
        producto = []
    elif opcion == 2:
        print("\t- Informe productos -")
        informeProducto()
    elif opcion == 3:
        menuAdmin()
        try:
            adm_opcion = int(input("-->"))
        except ValueError:
            print("Opcion ingresada invalida.")
        if adm_opcion == 1:
            print("Ingrese ID producto.")
            while True:
                try:
                    adm_id = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("ID ingresado invalido.")
            for prod in productos:
                if adm_id in prod:
                    print("Producto entrado. Desea eliminar? S/N")
                    s = input("-->")
                    if s.lower() == "s":
                        productos.remove(prod)
                    else:
                        break
            print("Producto eliminado satisfactoriamente.")
        elif adm_opcion == 2:
            print("Ingrese ID producto.")
            while True:
                try:
                    adm_id = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("ID ingresado invalido.")
            for prod in productos:
                if adm_id in prod:
                    print("""
                    Campo a modificar. 
                    Nombre  - 1 
                    Precio  - 2 
                    Stock   - 3
                    """)
                    opcion = int(input("-->"))
                    prod[opcion] = input("\n-->\t")
                    print("Producto modificado.")
                    break
        elif adm_opcion == 3:
            for prod in productos:
                p.append(prod[4])
            for x in productos:
                mayorVenta = max(p)
                if mayorVenta in x:
                    print(f"\t-PRODUCTO ID:\t{x[0]}")
                    print(f"\t-NOMBRE:\t{x[1]}")
    elif opcion == 4:
        informeProducto()
        print("Que producto desea comprar:")
        nombreProducto = input()
        for prod in productos:
            if nombreProducto in prod:
                print("Ingrese la cantidad que desea comprar.")
                cant = int(input("\n-->\t"))
                while cant > prod[3]:
                    print("No existe suficiente stock:")
                    cant = int(input("\n-->\t"))
                print(f"El valor del producto es:\t${prod[2]*cant}")
                s = input("Confirmar compra. S/N\n-->\t")
                if s.lower() == "s":
                    prod[4] = prod[4] + 1
                    prod[3] = prod[3] - cant
                else:
                    break
    elif opcion == 5:
        print("ADIOS....")
    else:
        print("Opcion ingresada invalida.")
