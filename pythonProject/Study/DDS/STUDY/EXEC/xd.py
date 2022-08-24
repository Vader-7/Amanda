registro = 0
menu = 0
print("********Bienvenido/a a la app de Juan Maestro********")
print('\n\t1. Registrar Cliente\n\t2. Suscripción\n\t3. Consultar Datos Cliente\n\t4. Salir')
menu = int(input("\nIngrese la opción que desea ==> "))
flag = 0
suscriptor = "suscrito"
while flag == 0:
    if menu == 1:
        print("***Bienvenido al  registro del cliente***")
        while True:
            try:
                rut = int(input("RUT sin puntos ni digito verificador ==> "))
                break
            except ValueError:
                print("Formato invalido.")
        while rut < 4000000 or rut > 99999999:
            print("Error en el dato ingresado")
            rut = int(input("RUT sin puntos ni digito verificador ==> "))

            nombre = input("Nombre ==> ")

            direccion = input("Dirección ==> ")

            comuna = input("Comuna ==> ")

            correo = input("Correo ==> ")
            while correo.count(".") == 0 or correo.count("@") == 0:
                print("Correo invalido, porfavor ingrese correctamense su correo")
                correo = input("Correo ==> ")

            edad = int(input("Edad ==> "))

            while edad < 0 or edad > 110:
                print("Error en el dato ingresado")
                edad = int(input("Edad ==> "))

            genero = input("Género: Masculino o Femenino u Otro (M o F u O) ==> ")
            while genero.lower() != "m" and genero.lower() != "f" and genero.lower() != "o":
                print("Error al registro de dato")
                genero = input("Género: Masculino o Femenino u Otro (M o F u O) ==> ")
            if genero.lower() == "m":
                genero = "Masculino"
            elif genero.lower() == "f":
                genero = "Femenino"
            elif genero.lower() == "o":
                genero = "Otro"

            tipo_suscrip = input("Tipos -> Premium - Gold - Silver: ")

            if tipo_suscrip.lower() != "premium" or tipo_suscrip.lower() != "gold" or tipo_suscrip.lower() != "silver":
                tipo_suscrip = suscriptor

            celular = int(input("Célular ==> "))

            print("Usted ha finalizado el registro del cliente, volverá al menu principal")
            print('\n\t1. Registrar Cliente\n\t2. Suscripción\n\t3. Consultar Datos Cliente\n\t4. Salir')
            menu = int(input("\nIngrese la opción que desea ==> "))
            print("***********************************************")

    elif menu == 2:
            print("*******Bienvenido al apartado de Suscripción********")
            print("***Porfavor ingrese su rut***")
            rutcliente = int(input("Rut ==> "))
            while rutcliente != rut:
                print("El rut ingresado no está registrado en el sistema")
                rutsuscrip = int(input("Ingrese nuevamente el rut: "))
            if rutcliente == rut:
                print("EL rut ingresado se encuentra registrado en el sistema")

            print("***ingrese la fecha con formato Día-Mes-Año***")
            fechasuscrip = input("Fecha actual: ")
            dia, mes, anio = map(int, fechasuscrip.split("-"))
            print('\n\t1. Registrar Cliente\n\t2. Suscripción\n\t3. Consultar Datos Cliente\n\t4. Salir')
            menu = int(input("\nIngrese la opción que desea ==> "))
            print("***********************************************")
    elif menu == 3:
        print("***Bienvenido a  la consulta de datos del cliente***")
        print("**Porfavor ingrese el rut del cliente**")
        rutsuscrip = int(input("Rut: "))
        while rutsuscrip != rut:
            print("El rut ingresado no está registrado en el sistema")
            rutsuscrip = int(input("Ingrese nuevamente el rut: "))

    if rut == rutsuscrip:
        print(
            f"\tNombre: {nombre}\n\tDirección: {direccion}\n\tComuna: {comuna}\n\tCorreo: {correo}\n\tEdad: {edad} años\n\tGénero: {genero}\n\tTipo de Suscripción: {tipo_suscrip}")
        print("*************************************************************************************")
        print('\n\t1. Registrar Cliente\n\t2. Suscripción\n\t3. Consultar Datos Cliente\n\t4. Salir')
        menu = int(input("\nIngrese la opción que desea ==> "))
        print("***********************************************")
    elif menu == 4:
        print("Gracias por suscribirse a la App de Juan Maestro")
        exit()
