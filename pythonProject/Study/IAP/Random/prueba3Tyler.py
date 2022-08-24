from datetime import date
fichas = 0
registros = 0
registro1 = None
registro2 = None
registro3 = None
rut1 = None
rut2 = None
rut3 = None
sexo1 = None
sexo2 = None
sexo3 = None
correo1 = None
correo2 = None
correo3 = None
edad1 = None
edad2 = None
edad3 = None
dirección1 = None
dirección2 = None
dirección3 = None
nombre1 = None
nombre2 = None
nombre3 = None
ps1 = None
ps2 = None
ps3 = None
opción: int = 0
opcionr: int = 0
today = date.today()

while opción != 4:
    print("\t\tCentro Médico DUOC")
    print("\n\t(1)\tRegistrar Paciente.")
    print("\t(2)\tAtención Paciente.")
    print("\t(3)\tConsultar Datos Paciente.")
    print("\t(4)\tSALIR.")
    try:
        opción = int(input("\t→\t"))
    except:
        print("\t\tOpción Ingresada Invalida, dígito un numero.")
    if opción == 1:
        if fichas < 3:
            if fichas == 0:
                rut1 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                while rut1 < 5000000 or rut1 > 999999999:
                    print("\t\tRUT INVALIDO")
                    rut1 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                print("\tRut registrado en el Sistema.")
                nombre1 = input("\tIngrese su nombre:\n\t->")
                dirección1 = input("\tIngrese su dirección:\n\t->")
                correo1 = input("\tIngrese su correo:\n\t->")
                contador = 0
                for i in correo1:
                    if i == "@":
                        contador = contador + 1
                while contador != 1:
                    print("\t\tError, mas de una @ registrada.\n\tCORREO INVALIDO.")
                    correo1 = input("\tIngrese su correo:\n\t->")
                    contador = 0
                    for i in correo1:
                        if i == "@":
                            contador = contador + 1
                edad1 = int(input("\tIngrese su edad:\n\t->"))
                while edad1 < 0 or edad1 > 110:
                    print("\tEdad ingresada invalida.")
                    edad1 = int(input("\tIngrese su edad:\n\t->"))
                sexo1 = input("\tIngrese su sexo (F) o (M):\n\t->")
                contas = 0
                for i in sexo1:
                    if i == "f":
                        contas = contas + 1
                    elif i == "F":
                        contas = contas + 1
                    elif i == "M":
                        contas = contas + 1
                    elif i == "m":
                        contas = contas + 1
                while contas != 1:
                    print("\tSexo ingresado invalido.")
                    sexo1 = input("\tIngrese su sexo (F) o (M):\n\t->")
                    contas = 0
                    for t in sexo1:
                        if t == "f":
                            contas = contas + 1
                        elif t == "F":
                            contas = contas + 1
                        elif t == "M":
                            contas = contas + 1
                        elif t == "m":
                            contas = contas + 1
                ps1 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                contaf = False
                for i in ps1:
                    if ps1 == "ISAPRE":
                        contaf = True
                    elif ps1 == "FONASA":
                        contaf = True
                while not contaf:
                    print("\tDato ingresado invalido, INGRESE SOLO EN MAYÚSCULAS.")
                    ps1 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                    contaf = False
                    for i in ps1:
                        if ps1 == "ISAPRE":
                            contaf = True
                        elif ps1 == "FONASA":
                            contaf = True
                print("Ficha Ingresada correctamente.")
                fichas = fichas + 1
            elif fichas == 1:
                rut2 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                while rut2 < 5000000 or rut1 > 999999999:
                    print("\t\tRUT INVALIDO")
                    rut2 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                print("\tRut registrado en el Sistema.")
                nombre2 = input("\tIngrese su nombre:\n\t->")
                dirección2 = input("\tIngrese su dirección:\n\t->")
                correo2 = input("\tIngrese su correo:\n\t->")
                contador = 0
                for i in correo2:
                    if i == "@":
                        contador = contador + 1
                while contador != 1:
                    print("\t\tError, mas de una @ registrada.\n\tCORREO INVALIDO.")
                    correo2 = input("\tIngrese su correo:\n\t->")
                    contador = 0
                    for i in correo2:
                        if i == "@":
                            contador = contador + 1
                edad2 = int(input("\tIngrese su edad:\n\t->"))
                while edad2 < 0 or edad2 > 110:
                    print("\tEdad ingresada invalida.")
                    edad2 = int(input("\tIngrese su edad:\n\t->"))
                sexo2 = input("\tIngrese su sexo (F) o (M):\n\t->")
                contas = 0
                for i in sexo2:
                    if i == "f":
                        contas = contas + 1
                    elif i == "F":
                        contas = contas + 1
                    elif i == "M":
                        contas = contas + 1
                    elif i == "m":
                        contas = contas + 1
                while contas != 1:
                    print("\tSexo ingresado invalido.")
                    sexo2 = input("\tIngrese su sexo (F) o (M):\n\t->")
                    contas = 0
                    for t in sexo2:
                        if t == "f":
                            contas = contas + 1
                        elif t == "F":
                            contas = contas + 1
                        elif t == "M":
                            contas = contas + 1
                        elif t == "m":
                            contas = contas + 1
                ps2 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                contaf = False
                for i in ps2:
                    if ps2 == "ISAPRE":
                        contaf = True
                    elif ps2 == "FONASA":
                        contaf = True
                while not contaf:
                    print("\tDato ingresado invalido, INGRESE SOLO EN MAYÚSCULAS.")
                    ps2 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                    contaf = False
                    for i in ps2:
                        if ps2 == "ISAPRE":
                            contaf = True
                        elif ps2 == "FONASA":
                            contaf = True
                print("Ficha Ingresada correctamente.")
                fichas = fichas + 1
            elif fichas == 2:
                rut3 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                while rut3 < 5000000 or rut1 > 999999999:
                    print("\t\tRUT INVALIDO")
                    rut3 = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->"))
                print("\tRut registrado en el Sistema.")
                nombre3 = input("\tIngrese su nombre:\n\t->")
                dirección3 = input("\tIngrese su dirección:\n\t->")
                correo3 = input("\tIngrese su correo:\n\t->")
                contador = 0
                for i in correo3:
                    if i == "@":
                        contador = contador + 1
                while contador != 1:
                    print("\t\tError, mas de una @ registrada.\n\tCORREO INVALIDO.")
                    correo3 = input("\tIngrese su correo:\n\t->")
                    contador = 0
                    for i in correo3:
                        if i == "@":
                            contador = contador + 1
                edad3 = int(input("\tIngrese su edad:\n\t->"))
                while edad3 < 0 or edad3 > 110:
                    print("\tEdad ingresada invalida.")
                    edad3 = int(input("\tIngrese su edad:\n\t->"))
                sexo3 = input("\tIngrese su sexo (F) o (M):\n\t->")
                contas = 0
                for i in sexo3:
                    if i == "f":
                        contas = contas + 1
                    elif i == "F":
                        contas = contas + 1
                    elif i == "M":
                        contas = contas + 1
                    elif i == "m":
                        contas = contas + 1
                while contas != 1:
                    print("\tSexo ingresado invalido.")
                    sexo3 = input("\tIngrese su sexo (F) o (M):\n\t->")
                    contas = 0
                    for t in sexo3:
                        if t == "f":
                            contas = contas + 1
                        elif t == "F":
                            contas = contas + 1
                        elif t == "M":
                            contas = contas + 1
                        elif t == "m":
                            contas = contas + 1
                ps3 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                contaf = False
                for i in ps3:
                    if ps3 == "ISAPRE":
                        contaf = True
                    elif ps3 == "FONASA":
                        contaf = True
                while not contaf:
                    print("\tDato ingresado invalido, INGRESE SOLO EN MAYÚSCULAS.")
                    ps3 = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                    contaf = False
                    for i in ps3:
                        if ps3 == "ISAPRE":
                            contaf = True
                        elif ps3 == "FONASA":
                            contaf = True
                print("Ficha Ingresada correctamente.")
                fichas = fichas + 1
        else:
            print("\n\t\tNumero de registros máximos alcanzado.\n\tHASTA PRONTO.")
    if opción == 2:
        if fichas == 0:
            print("\tNo se han creado fichas en nuestro sistema, registraste plx.")
        else:
            print("\n\t\tATENCIÓN DEL PACIENTE.")
            var = int(input("\t\tIngrese su Rut para consultar en sistema: "))
            if registros < 6:
                if rut1 == var:
                    print(f"\t\tIngrese sus observaciones de la consulta del día {today}")
                    registro1 = input("\n\t\t->\t")
                    registros = registros + 1
                elif rut2 == var:
                    print(f"\t\tIngrese sus observaciones de la consulta del día {today}")
                    registro2 = input("\n\t\t->\t")
                    registros = registros + 1
                elif rut3 == var:
                    print(f"\t\tIngrese sus observaciones de la consulta del día {today}")
                    registro3 = input("\n\t\t->\t")
                    registros = registros + 1
                else:
                    print("\t\tRUT NO EXISTE EN SISTEMA...\n")
            else:
                print("Atenciones máximas alcanzadas.")
    if opción == 3:
        if fichas == 0:
            print("\tNo se han creado fichas en nuestro sistema, registraste plx.")
        else:
            var = int(input("\t\tIngrese su Rut para consultar en sistema: "))
            if rut1 == var:
                print("\n\t\tInformación del Rut consultado:\n")
                print(f"\tRut:\t\t\t{rut1}")
                print(f"\tNombre:\t\t\t{nombre1}")
                print(f"\tDirección:\t\t{dirección1}")
                print(f"\tCorreo:\t\t\t{correo1}")
                print(f"\tEdad:\t\t\t{edad1}")
                print(f"\tSexo:\t\t\t{sexo1}")
                print(f"\tNro de Ficha:\t{fichas}")
                print(f"\tAfiliación:\t\t{ps1}")
                print(f"\tRegistro de consulta:\t{registro1}.\tFecha:\t{today}")
            elif rut2 == var:
                print("\n\t\tInformación del Rut consultado:\n")
                print(f"\tRut:\t\t\t{rut2}")
                print(f"\tNombre:\t\t\t{nombre2}")
                print(f"\tDirección:\t\t{dirección2}")
                print(f"\tCorreo:\t\t\t{correo2}")
                print(f"\tEdad:\t\t\t{edad2}")
                print(f"\tSexo:\t\t\t{sexo2}")
                print(f"\tNro de Ficha:\t{fichas}")
                print(f"\tAfiliación:\t\t{ps2}")
                print(f"\tRegistro de consulta:\t{registro2}.\tFecha:\t{today}")
            elif rut3 == var:
                print("\n\t\tInformación del Rut consultado:\n")
                print(f"\tRut:\t\t\t{rut3}")
                print(f"\tNombre:\t\t\t{nombre3}")
                print(f"\tDirección:\t\t{dirección3}")
                print(f"\tCorreo:\t\t\t{correo3}")
                print(f"\tEdad:\t\t\t{edad3}")
                print(f"\tSexo:\t\t\t{sexo3}")
                print(f"\tNro de Ficha:\t{fichas}")
                print(f"\tAfiliación:\t\t{ps3}")
                print(f"\tRegistro de consulta:\t{registro3}.\tFecha:\t{today}")
            else:
                print("\t\tRUT NO EXISTE EN SISTEMA...\n")
    if opción == 4:
        print("\n\t\tHa salido del sistema....\n\t\tHASTA PRONTO.")
        break