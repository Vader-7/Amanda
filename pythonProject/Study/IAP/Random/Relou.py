# VARIABLES
opcion = 0
sumaNotas = 0
promedio = 0
user = "ProfeAndriu"
# RANGO x USUARIO
while opcion != 2:
    print("""
        1.- CALCULAR PROMEDIO ALUMNO.
        2.- SALIR.
        """)
    # CONTROL POR EXCEPCIÓN
    try:
        opcion = int(input("\n--->\t"))
    except ValueError:
        print("OPCION INVALIDA.")
    if opcion == 1:
        print("INGRESE USUARIO")
        us = input("\n-->\t")
        if us != user:
            print("NO ES PROFE.")
        else:
            print("INGRESE LA CANTIDAD DE NOTAS:")
            cantNotas = int(input("\n-->\t"))
            # CICLO PARA CALCULAR TOTAL NOTAS
            for i in range(cantNotas):
                print(f"INGRESE LA {i + 1} NOTA:")
                nota = int(input("\n-->\t"))
                # VALIDA LARGO DE NOTA
                # CASTEA DE INT A STR PARA SABER EL LARGO DE LA CADENA
                while len(str(nota)) > 2:
                    print("NOTA INGRESADA INVALIDA.")
                    print(f"INGRESE LA {i + 1} NOTA:")
                    nota = int(input("\n-->\t"))
                sumaNotas = sumaNotas + nota
            # CALCULA PROMEDIO
            promedio = round(sumaNotas/cantNotas)
            # IMPRIME PROMEDIO
            print(f"EL PROMEDIO DEL ALUMNO ES:\t{promedio}")
            # IF PARA CALCULAR SI APROBO
            # TEST WHILE XD
            while True:
                if promedio < 40:
                    print("REPROBADO.")
                elif promedio > 40:
                    print("APROBADO.")
                    break
    elif opcion == 2:
        print("ADIOS.")
        break
    else:
        print("OPCION INGRESADA INVALIDA.")
