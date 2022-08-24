# MATERIAL COMPLEMENTARIO
# VARIABLES
opcion = 0
valor_menor = 4000
valor_adulto = 7000
valor_adulto_mayor = 3000
valor_compra = 0
total_compras_x_dia = 0
total_personas_x_dia = 0
cont_menor = 0
cont_adulto = 0
cont_mayor = 0
while opcion != 2:
    print("""
            COMPRAS BOLETO
            1.- INGRESAR COMPRA.
            2.- SALIR.    
        """)
    opcion = int(input("\n-->\t"))
    if opcion == 1:
        print("CUANTAS PERSONAS DESEA INGRESAR.")
        cant = int(input("\n-->\t"))
        for i in range(cant):
            print(f"INGRESE LA EDAD DE LA {i + 1} PERSONA.")
            edad = int(input("\n-->\t"))
            if 7 < edad < 12:
                valor_compra += valor_menor
                cont_menor += 1
            elif 12 <= edad <= 65:
                valor_compra += valor_adulto
                cont_adulto += 1
            elif edad > 65:
                valor_compra += valor_adulto_mayor
                cont_mayor += 1
        total_compras_x_dia += valor_compra
        total_personas_x_dia += cant
        print(f"""
            ------------------------------------
            {cont_menor} MENOR(S):\t\t\t$4.000
            {cont_adulto} ADULTO(S):\t\t$7.000
            {cont_mayor} ADULTO MAYOR(S):\t$3.000
            ------------------------------------
            TOTAL:\t\t${valor_compra}
            """)
    if opcion == 2:
        print(f"EL TOTAL DE DINERO ACUMULADO DURANTE EL DIA ES:\t${total_compras_x_dia}")
        print(f"EL TOTAL DE PERSONAS QUE ASISTIERON DURANTE EL DIA ES:\t{total_personas_x_dia}")