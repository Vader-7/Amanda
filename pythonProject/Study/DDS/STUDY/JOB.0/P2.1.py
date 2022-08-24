# TUTORIA 1 LUNES EXEC (PRUEBA.2)
# IMPORT RE PARA VALIDAR CORREO
import valida
import re
# IMPORT DATETIME PARA VALIDAR FECHA
from datetime import datetime


# MENU
def menu():
    print("""
                1.- REGISTRAR CLIENTE.
                2.- SUSCRIPCIÓN.
                3.- CONSULTAR DATOS CLIENTE.
                4.- SALIR.
                """)


# VALIDA
def valida(p_campo):
    while p_campo is None or p_campo == "":
        print("DATO INGRESADO INVALIDO.")
        p_campo = input("\n-->\t")


# VARIABLES DE COMPARACION
sexo0 = "F"
sexo1 = "M"
tipo0 = "PREMIUM"
tipo1 = "GOLD"
tipo2 = "SILVER"
# VARIABLES PARA EL REGISTRO(RETULIZACIÓN)
opcion = 0
clientes = []
cliente = []
# MENU
while opcion != 4:
    menu()
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
            print("INGRESE NOMBRE")
            nombre = input("\n-->\t")
            while len(nombre) < 3:
                print("NOMBRE INGRESADO INVALIDO.")
                nombre = input("\n-->\t")
            print("INGRESE SU DIRECCION.")
            direccion = input("\n-->\t")
            valida(direccion)
            print("INGRESE SU COMUNA.")
            comuna = input("\n-->\t")
            valida(comuna)
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
            cliente = ["SUSCRITO DESDE: ", str(rut), nombre, direccion, comuna, correo, edad, genero, celular, tipo]
            clientes.append(cliente)
        elif opcion == 2:
            # PREGUNTAMOS RUT PARA VALIDAR SI ESTA REGISTRADO
            print("INGRESE RUT A CONSULTAR.")
            rut = input("\n-->\t")
            for c in clientes:
                if rut not in c:
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
                            cliente[0] = cliente[0] + fecha
                            break
                        except ValueError:
                            print("FECHA INVALIDA.")
        elif opcion == 3:
            print("INGRESE RUT A CONSULTAR.")
            rut = input("\n-->\t")
            for c in clientes:
                if rut not in c:
                    print("RUT INGRESADO NO SE ENCUENTRA REGISTRADO EN SISTEMA.")
                elif "SUSCRITO DESDE: " in c:
                    print("FECHA NO SE ENCUENTRA REGISTRADA EN SISTEMA.")
                else:
                    for cl in c:
                        print(f"*\t{cl}")
        elif opcion == 4:
            print("GRACIAS POR SUBSCRIBIRSE A JUAN MAESTRO…\nADIOS.")
            break
        else:
            print("\nOPCION INGRESADA INVALIDA.")
    except ValueError:
        print("\nOPCION INGRESADA INVALIDA.")
