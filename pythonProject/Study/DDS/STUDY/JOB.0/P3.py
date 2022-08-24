# MATERIAL COMPLEMENTARIO TUTORIAS TYLER
from datetime import datetime
import valida

# CONSTANTES
tipo0 = "B"
tipo1 = "D"
tipo2 = "E"
tipo3 = "H"
# VARIABLES
opcion = 0
patente = 0
ver_patente = None
registros = None
ver_tipo = None
marca = None
modelo = None
anio = None

while opcion != 4:
    print("""
            1.- REGISTRAR AUTOMOVIL.
            2.- REGISTRAR MANTENIMIENTO.
            3.- CONSULTAR AUTOMOVIL.
            4.- SALIR.
        """)
    try:
        opcion = int(input("\n-->\t"))
        if opcion == 1:
            while True:
                print("INGRESE PATENTE.")
                patente = input("\n-->\t")
                if re.match(r"(^[A-Z]{2}\d{4})", patente):
                    print("PATENTE REGISTRADA.")
                    ver_patente = patente
                    break
                elif re.match(r"(^[A-Z]{4}\d{2})", patente):
                    print("PATENTE REGISTRADA.")
                    ver_patente = patente
                    break
                else:
                    print("PATENTE INVALIDO.\n")
                print(ver_patente)
            # MARCA
            print("INGRESE MARCA DEL AUTO.")
            marca = input("\n-->\t")
            while marca is None or marca == "":
                print("OPCION INGRESADA INVALIDA")
                marca = input("\n-->\t")
            # MODELO
            print("INGRESE MODELO DEL AUTO.")
            modelo = input("\n-->\t")
            while modelo is None or modelo == "":
                print("OPCION INGRESADA INVALIDA")
                modelo = input("\n-->\t")
            # VALIDA TIPO DE DATO AÑO
            while True:
                try:
                    print("INGRESE EL AÑO DE FABRICACIÓN.")
                    anio = int(input("\n-->\t"))
                    break
                except ValueError:
                    print("AÑO INVALIDA.")
            # VALIDA RANGOS DEL AÑO
            while anio < 1900 or anio > 2021:
                print("OPCIÓN INGRESADA INVALIDA.")
                anio = int(input("\n-->\t"))
            # VALIDA TIPO
            print("""
                    INGRESE EL TIPO DEL AUTO.

                    B.- BENCINA.
                    D.- DIESEL.
                    E.- ELECTRICO.
                    H.- HIBRIDO.
                    """)
            tipo = input("\n-->\t")
            while True:
                if tipo.upper() != tipo0 and tipo.upper() != tipo1 and tipo.upper() != tipo2 and tipo.upper() != tipo3:
                    print("OPCION INGRESADA INVALIDA")
                    tipo = input("\n-->\t")
                else:
                    print("TIPO REGISTRADO.")
                    if tipo.upper() == tipo0:
                        ver_tipo = "BENCINA"
                        break
                    elif tipo.upper() == tipo1:
                        ver_tipo = "DIESEL"
                        break
                    elif tipo.upper() == tipo2:
                        ver_tipo = "ELÉCTRICO"
                        break
                    elif tipo.upper() == tipo3:
                        ver_tipo = "HÍBRIDO"
                        break
            print("\nAUTO REGISTRADO.")
        elif opcion == 2:
            print("INGRESE LA PATENTE A CONSULTAR.")
            patente = input("\n-->\t")
            if patente != ver_patente:
                print("PATENTE NO REGISTRADA EN SISTEMA.")
            else:
                while True:
                    try:
                        fecha = input("INGRESA LA FECHA DE LA REVISION. (DD-MM-YYYY)\n-->\t ")
                        # VALIDA SEGUN FORMATO ESTABLECIDO
                        datetime.strptime(fecha, '%d-%m-%Y')
                        print("FECHA ASIGNADA.")
                        # GUARDAMOS FECHA
                        print("INGRESE LAS OBSERVACIONES.")
                        obs = input("\n-->\t")
                        registros = "REGISTRO:\t\t" + fecha + "\n" + "\t\t\t\t\tOBSERVACIONES:\t" + obs
                        break
                    except ValueError:
                        print("FECHA INVALIDA.")
        elif opcion == 3:
            print("INGRESE LA PATENTE A CONSULTAR.")
            patente = input("\n-->\t")
            if patente != ver_patente:
                print("PATENTE NO REGISTRADA EN SISTEMA.")
            elif registros is None:
                print("FECHA Y OBSERVACIONES NO REGISTRADOS EN SISTEMA.")
            else:
                print(f"""
                    {registros}
                    -------------------------
                    PATENTE\t\t\t{ver_patente}
                    MARCA:\t\t\t{marca}
                    MODELO:\t\t\t{modelo}
                    AÑO:\t\t\t{anio}
                    TIPO:\t\t\t{ver_tipo}
                    -------------------------
                    """)
        elif opcion == 4:
            print("CERRANDO SESIÓN.")
        else:
            print("OPCION INGRESADA INVALIDA.")
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
