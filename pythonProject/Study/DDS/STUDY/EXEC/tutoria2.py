from os import system
system("clear")
# VARIABLES.
opcion = 0
menor = 4000
adulto = 7000
adulto_mayor = 3000
cont_menor = 0
cont_adulto = 0
cont_adulto_mayor = 0
monto_total = 0
cantidad_total_dinero = 0
cantidad_total_personas = 0
# ALGORITMO.
# MENU.
while opcion != 2:
    print("""
            1.-   INGRESAR COMPRA.
            2.-   SALIR.
            """)
    opcion = int(input("\n-->\t"))
    # SALIDA OPCION 1 MENU.
    if opcion == 1:
        while True:
            # EXCEPTIONS CANTIDAD.
            try:
                cantidad = int(input("Cuantas entradas va comprar.\n-->\t"))
                break
            except ValueError:
                print("Dato ingresado invalido.")
                # CALCULA PRECIO x EDAD
        for i in range(cantidad):
            edad = int(input(f"{i + 1}. Ingrese su edad.\n-->\t"))
            if 7 < edad > 12:
                monto_total = monto_total + menor
                cont_menor += 1
            elif 12 <= edad >= 65:
                monto_total = monto_total + adulto
                cont_adulto += 1
            elif edad > 65:
                monto_total = monto_total + adulto_mayor
                cont_adulto_mayor += 1
        # CONTADOR TOTAL DINERO Y PERSONAS x CICLO
        cantidad_total_dinero += monto_total
        cantidad_total_personas += cantidad
        print(f"""
              -----------------------------------------
              {cont_menor} Menor(s):\t\t\t$4000
              {cont_adulto} Adulto(s):\t\t\t$7000
              {cont_adulto_mayor} Adulto Mayor(s):\t$3000
              -----------------------------------------
              Total: ${monto_total}
              """)
        # REINICIA VARIABLES x OPCION
        cont_menor = 0
        cont_adulto = 0
        cont_adulto_mayor = 0
    # SALIDA OPCION 2 MENU.
    if opcion == 2:
        # IMPRIME CANTIDAD TOTAL DINERO Y PERSONAS x DIA
        print(f"El monto total recaudado durante el día es: ${cantidad_total_dinero}")
        print(f"La cantidad de personas durante el dia fueron: {cantidad_total_personas}")
