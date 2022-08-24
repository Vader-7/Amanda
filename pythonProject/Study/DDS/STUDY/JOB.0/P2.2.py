# DESAFIO CON LISTAS
# TUTORIA 1 LUNES EXEC (PRUEBA.2)
# IMPORT RE PARA VALIDAR CORREO
import valida
# IMPORT DATETIME PARA VALIDAR FECHA
from datetime import datetime

# VARIABLES DE COMPARACION
sexo0 = "F"
sexo1 = "M"
tipo0 = "PREMIUM"
tipo1 = "GOLD"
tipo2 = "SILVER"
# VARIABLES PARA EL REGISTRO(RETULIZACIÓN)
opcion = 0
registro = []
# MENU
while opcion != 4:
    print("""
            1.- REGISTRAR CLIENTE.
            2.- SUSCRIPCIÓN.
            3.- CONSULTAR DATOS CLIENTE.
            4.- SALIR.
            """)
    try:
        opcion = int(input("\n-->\t"))
        if opcion == 1:
            # VALIDA TIPO DE DATO RUT
            while True:
                try:
                    print("INGRESE SU RUT.")
                    rut = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("RUT INGRESADO INVALIDO.")
            # VALIDA RANGOS DEL RUT
            while rut < 4000000 or rut > 99999999:
                print("RUT INGRESADO INVALIDO.")
                rut = int(input("\n-->\t"))
            # ASIGNA RUT VERIFICADO
            # VALIDA NOMBRE
            while True:
                print("INGRESE NOMBRE.")
                nombre = input("\n-->\t")
                # ISALPHA DEVUELVE TRUE SI LA CADENA ES ALFABÉTICA
                if not nombre.isalpha():
                    print("NOMBRE INGRESADO INVALIDO.\n")
                else:
                    print("NOMBRE INGRESADO.")
                    break
            while len(nombre) < 3:
                print("NOMBRE INGRESADO INVALIDO.")
                nombre = input("\n-->\t")
            print("INGRESE SU DIRECCION.")
            direccion = input("\n-->\t")
            print("INGRESE SU COMUNA.")
            comuna = input("\n-->\t")
            while True:
                print("INGRESE CORREO.")
                correo = input("\n-->\t")
                if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", correo):
                    print("CORREO VALIDO.\n")
                    break
                else:
                    print("CORREO INVALIDO.\n")
            # VALIDA EDAD
            while True:
                try:
                    print("INGRESE SU EDAD.")
                    edad = int(input("\n-->\t"))
                    while edad < 0 or edad > 110:
                        print("EDAD ES INVALIDA.")
                        edad = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("DATO INGRESADO INVALIDO.")
            # VALIDA GENERO
            print("""
                    INGRESE SU GENERO\n
                    F - PARA FEMENINO.
                    M - PARA MASCULINO.
                    """)
            genero = input("\n-->\t")
            while genero != sexo0 and genero != sexo1:
                print("OPCION INGRESADA INVALIDA.")
                genero = input("\n-->\t")
            # VALIDA CELULAR
            print("INGRESE SU CELULAR EJEMPLO (98544756).")
            celular = input("\n-->\t")
            while celular[0] != 9 and len(celular) < 8:
                print("CELULAR INGRESADO INVALIDO")
                celular = input("\n-->\t")
            # VALIDA TIPO SUBSCRIPCIÓN
            print("""
                    INGRESE SU TIPO DE SUB\n
                    PREMIUM - GOLD - SILVER.
                    """)
            tipo = input("\n-->\t")
            while tipo != tipo0 and tipo != tipo1 and tipo != tipo2:
                print("OPCION INGRESADA INVALIDA.")
                tipo = input("\n-->\t")
            print("\n\tREGISTRO REALIZADO CON EXITO.")
            print(len(registro))

            registro = ["SUSCRITO ", rut, nombre, direccion, comuna, correo, celular, genero, tipo]
        if opcion == 2:
            # PREGUNTAMOS RUT PARA VALIDAR SI ESTA REGISTRADO
            print("INGRESE RUT A CONSULTAR.")
            rut = int(input("\n-->\t"))
            if registro[1] != rut:
                print("RUT INGRESADO NO SE ENCUENTRA REGISTRADO EN SISTEMA.")
            else:
                # VALIDAMOS FORMATO FECHA Y FECHA VALIDA
                while True:
                    try:
                        fecha = input("INGRESA LA FECHA DE LA SUBSCRIPCIÓN. (DD-MM-YYYY)\n-->\t ")
                        # VALIDA SEGUN FORMATO ESTABLECIDO
                        datetime.strptime(fecha, '%d-%m-%Y')
                        print("FECHA ASIGNADA.")
                        # GUARDAMOS FECHA
                        registro.append(fecha)
                        break
                    except ValueError:
                        print("FECHA INVALIDA.")
        if opcion == 3:
            print("INGRESE RUT A CONSULTAR.")
            rut = int(input("\n-->\t"))
            if rut != registro[1]:
                print("NO SE ENCUENTRAN REGISTROS DEL RUT INGRESADO.")
            if len(registro) < 11:
                print("NO SE ENCUENTRA FECHA DE SUBSCRIPCIÓN EN SISTEMA, POR FAVOR REGISTRAR (OPCIÓN 2)")
            else:
                print(f"""
                        INFORME DE:\t\t{registro[2]}
                        {registro[0]} DESDE: {registro[10]}
                        ---------------------------
                        RUT:\t\t\t{registro[1]}
                        DIRECCIÓN:\t\t{registro[3]}
                        COMUNA:\t\t\t{registro[4]}
                        CORREO:\t\t\t{registro[5]}
                        EDAD:\t\t\t{registro[6]}
                        GENERO:\t\t\t{registro[7]}
                        CELULAR:\t\t{registro[8]}
                        TIPO:\t\t\t{registro[9]}
                        ---------------------------
                        """)
        if opcion == 4:
            print("GRACIAS POR SUBSCRIBIRSE A JUAN MAESTRO…\nADIOS.")
            break
        else:
            print("\nOPCION INGRESADA INVALIDA.")
    except ValueError:
        print("\nOPCION INGRESADA INVALIDA.")
