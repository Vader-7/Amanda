# TUTORIA 2 VIERNES EXEC (PRUEBA.2)
# IMPORTAMOS RE PARA VALIDAR CORREO
import re
# IMPORTAMOS DATETIME PARA VALIDAR FECHA(NO ES NECESARIO)
from datetime import datetime

opcion = 0
# USAREMOS ESTAS VARIABLES PARA VALIDAR MAS ADELANTE
sexo = {
    "1": "F",
    "2": "M"
}
subscripcion0 = "PREMIUM"
subscripcion1 = "GOLD"
subscripcion2 = "SILVER"
sub = "SUSCRITO"
# DEFINIMOS VARIABLES PARA REUTILIZARLAS
ver_rut = 0
ver_fecha = datetime
nombre = None
correo = None
direccion = None
comuna = None
edad = 0
celular = None
tipo = None

while opcion != 4:
    try:
        print("""
                1.- REGISTRAR CLIENTE.
                2.- SUSCRIPCIÓN.
                3.- CONSULTAR DATOS CLIENTES.
                4.- SALIR.
                """)
        opcion = int(input("\n-->\t"))
        if opcion == 1:
            # EXCEPCIÓN TIPO DE DATO INGRESADO
            while True:
                try:
                    print("INGRESE RUT.")
                    rut = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("RUT INGRESADO INVALIDO.\n")
            # VALIDA X RANGOS EL RUT
            while rut < 4000000 or rut > 99999999:
                print("RUT INGRESADO INVALIDO.\n")
                print("INGRESE RUT.")
                rut = int(input("\n-->\t"))
            ver_rut = rut
            # VALIDA QUE NO SE ENCUENTREN DIGITOS EN EL NOMBRE
            while True:
                print("INGRESE NOMBRE.")
                nombre = input("\n-->\t")
                # ISALPHA DEVUELVE TRUE SI LA CADENA ES ALFABÉTICA
                if not nombre.isalpha():
                    print("NOMBRE INGRESADO INVALIDO.\n")
                else:
                    break
            # NO PEDIA VALIDAR ESTOS
            print("INGRESE DIRECCION.")
            direccion = input("\n-->\t")
            print("INGRESE COMUNA.")
            comuna = (input("\n-->\t"))
            # VALIDA CORREO
            while True:
                print("INGRESE CORREO.")
                correo = input("\n-->\t")
                if re.match(r"(^[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z\d-.]+$)", correo):
                    print("CORREO VALIDO.\n")
                    break
                else:
                    print("CORREO INVALIDO.\n")
            # EXCEPCIÓN TIPO DE DATO INGRESADO
            while True:
                try:
                    print("INGRESE EDAD.")
                    edad = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("EDAD INGRESADA INVALIDA.\n")
            # VALIDA RANGOS DE EDAD
            while edad < 0 or edad > 110:
                print("EDAD INGRESADA INVALIDA.\n")
                print("INGRESE EDAD.")
                edad = int(input("\n-->\t"))
            # VALIDA SEXO INGRESADO VALIDO M/F
            print("""INGRESE SEXO"
                  1: M.
                  2: F.""")
            sexo = input("\n-->\t")
            while sexo not in "12":
                print("SEXO INGRESADO INVALIDO.\n")
                print("""INGRESE SEXO"
                                  1: M.
                                  2: F.""")
                sexo = input("\n-->\t")
            # VALIDA CELULAR PARECIDO A UN EJERCICIO QUE VÍ, POR SI LES APARECE EN LA PRUEBA.
            print("INGRESE SU CELULAR EJEMPLO (98544756)")
            celular = input("\n-->\t")
            # AQUÍ VALIDA EL LARGO DEL CELULAR Y SI EMPIEZA CON 9
            while len(celular) < 9 or celular[0] != "9":
                print("CELULAR INGRESADO INVALIDO.\n")
                print("INGRESE SU CELULAR.")
                celular = input("\n-->\t")
            print("""
                    INGRESE TIPO DE SUBSCRIPCIÓN.
                    (PREMIUM-GOLD-SILVER)""")
            tipo = input("\n-->\t")
            # VALIDAMOS EL TIPO CON LAS VARIABLES YA DEFINIDAS AL PRINCIPIO, SEGUN ESTO (cadena de caracteres que
            # sólo acepta los valores “PREMIUM” “GOLD” y “SILVER”)
            while tipo != subscripcion0 and tipo != subscripcion1 and tipo != subscripcion2:
                print("TIPO INGRESADO INVALIDO.\n")
                print("""
                        INGRESE TIPO DE SUBSCRIPCIÓN.
                        (PREMIUM-GOLD-SILVER)""")
                tipo = input("\n-->\t")
            print("\nUSUARIO REGISTRADO.")
        if opcion == 2:
            # PREGUNTAMOS RUT PARA VALIDAR SI ESTA REGISTRADO
            print("INGRESE RUT A CONSULTAR.")
            rut = int(input("\n-->\t"))
            if ver_rut != rut:
                print("RUT INGRESADO NO SE ENCUENTRA REGISTRADO EN SISTEMA.")
            else:
                # VALIDAMOS FORMATO FECHA Y FECHA VALIDA
                while True:
                    try:
                        fecha = input("INGRESA LA FECHA DE LA SUBSCRIPCIÓN. (DD-MM-YYYY)\n-->\t ")
                        datetime.strptime(fecha, '%d-%m-%Y')
                        print("FECHA ASIGNADA.")
                        # GUARDAMOS FECHA
                        ver_fecha = fecha
                        break
                    except ValueError:
                        print("FECHA INVALIDA.")

        if opcion == 3:
            # PREGUNTAMOS RUT PARA VALIDAR SI ESTA REGISTRADO
            print("INGRESE RUT A CONSULTAR.")
            rut = int(input("\n-->\t"))
            if ver_rut != rut:
                print("RUT INGRESADO NO SE ENCUENTRA REGISTRADO EN SISTEMA.")
            else:
                # IMPRIMIMOS INFORME
                print(f"""
                FECHA SUBSCRIPCIÓN:\t\t{ver_fecha}
                DATOS CLIENTE:\t\t\t{nombre}
                ---------------------------------
                    RUT:\t\t\t{ver_rut}
                    DIRECCIÓN:\t\t{direccion}
                    COMUNA:\t\t\t{comuna}
                    CORREO:\t\t\t{correo}
                    EDAD:\t\t\t{edad}
                    SEXO:\t\t\t{sexo}
                    CELULAR:\t\t{celular}
                    TIPO:\t\t\t{tipo}
                    ESTADO:\t\t\t{sub}
                ---------------------------------    
                    """)
        if opcion == 4:
            print("Gracias por suscribirse a la App de Juan Maestro…")
    except ValueError:
        print("SELECCIONA UNA OPCION VALIDA.\n")
