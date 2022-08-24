from datetime import date
registros = 0
ficha = 0
rut = None
edad = 0
opcion: int = 0
sexo = None
s1 = "f"
s2 = "F"
s3 = "m"
s4 = "M"
ps = None
f1 = "FONASA"
f2 = "ISAPRE"
correo = None
nombre = None
direccion = None
today = date.today()

while opcion != 4:
    print("\t\tCentro Médico DUOC")
    print("\n\t(1)\tRegistrar Paciente.")
    print("\t(2)\tAtención Paciente.")
    print("\t(3)\tConsultar Datos Paciente.")
    print("\t(4)\tSALIR.")
    try:
        opcion = int(input("\t→\t"))
    except:
        print("\t\tOpción Ingresada Invalida, digite un numero.")
    if opcion == 1:
        if registros < 1:
            if registros == 0:
                rut = int(input("\tIngrese su RUT, solo numeros sin guión ni coma.\n\t->"))
                while rut < 5000000 or rut > 999999999:
                    print("\t\tRUT INVALIDO")
                    rut = int(input("\tIngrese su RUT, solo numeros sin guión ni coma.\n\t->"))
                print("\tRut registrado en el Sistema.")
                nombre = input("\tIngrese su nombre:\n\t->")
                direccion = input("\tIngrese su dirección:\n\t->")
                correo = input("\tIngrese su correo:\n\t->")
                contador = 0
                for i in correo:
                    if i == "@":
                        contador = contador + 1
                while contador != 1:
                    print("\t\tError, mas de una @ registrada.\n\tCORREO INVALIDO.")
                    correo = input("\tIngrese su correo:\n\t->")
                    contador = 0
                    for i in correo:
                        if i == "@":
                            contador = contador + 1
                edad = int(input("\tIngrese su edad:\n\t->"))
                while edad < 0 or edad > 110:
                    print("\tEdad ingresada invalida.")
                    edad = int(input("\tIngrese su edad:\n\t->"))
                sexo = input("\tIngrese su sexo (F) o (M):\n\t->")
                contas = 0
                while contas == 0:
                    if sexo == s1:
                        contas = contas + 1
                    if sexo == s2:
                        contas = contas + 1
                    if sexo == s3:
                        contas = contas + 1
                    if sexo == s4:
                        contas = contas + 1
                    else:
                        print("\tSexo ingresado invalido.")
                        sexo = input("\tIngrese su sexo (F) o (M):\n\t->")
                        if sexo == s1:
                            contas = contas + 1
                        if sexo == s2:
                            contas = contas + 1
                        if sexo == s3:
                            contas = contas + 1
                        if sexo == s4:
                            contas = contas + 1
                ps = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                contaf = 0
                while contaf == 0:
                    if ps == f1:
                        contaf = contaf + 1
                    if ps == f2:
                        contaf = contaf + 1
                    else:
                        print("\tDato ingresado invalido, INGRESE SOLO EN MAYUSCULAS.")
                        ps = input("Ingrese a que filial pertenece (FONASA) o (ISAPRE):\n\t->")
                        if ps == f1:
                            contaf = contaf + 1
                        if ps == f2:
                            contaf = contaf + 1
                print("Ficha Ingresada correctamente.")
                ficha = ficha + 1
    if opcion == 2:
        if ficha == 0:
            print("\tNo se han creado fichas en nuestro sistema, registrese plx.")
        else:
            print("\n\t\tATENCION DEL PACIENTE.")
            var = int(input("\t\tIngrese su Rut para consultar en sistema: "))
            if rut == var:
                print(f"\t\tIngrese sus observaciones de la consulta del día {today}")
                registros = input("\n\t\t->\t")
            else:
                print("\t\tRUT NO EXISTE EN SISTEMA...\n")
    if opcion == 3:
        if ficha == 0:
            print("\tNo se han creado fichas en nuestro sistema, registrese plx.")
        else:
            var = int(input("\t\tIngrese su Rut para consultar en sistema: "))
            if rut == var:
                print("\n\t\tInformación del Rut consultado:\n")
                print(f"\tRut:\t\t\t{rut}")
                print(f"\tNombre:\t\t\t{nombre}")
                print(f"\tDirección:\t\t{direccion}")
                print(f"\tCorreo:\t\t\t{correo}")
                print(f"\tEdad:\t\t\t{edad}")
                print(f"\tSexo:\t\t\t{sexo}")
                print(f"\tNro de Ficha:\t{ficha}")
                print(f"\tAfiliación:\t\t{ps}")
                print(f"\tRegistro de consulta:\t{registros}.\tFecha:\t{today}")
            else:
                print("\t\tRUT NO EXISTE EN SISTEMA...\n")
    if opcion == 4:
        print("\n\t\tHa salido del sistema....\n\t\tHASTA PRONTO.")
        break
