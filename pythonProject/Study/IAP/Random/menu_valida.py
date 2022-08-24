opcion = 0
user = 0  # --> nos permite crear un usuario nuevo
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None
# creamos las variables sin asignacion aun para los usuarios
while opcion != 3:  # mientras no sea 3 la opcion, el while verdadero y seguira mostrando el menu
    print("\tMi menu")
    print("1)Iniciar Sesión")
    print("2)Registrar Usuario")
    print("3)Salir")
    try:
        opcion = int(input("→"))
    except ValueError:
        print("Debe ingresar sólo números")
    if opcion == 1:
        if user == 0:  # partio con asignación 0
            print("Debe crear un usuario")
        else:
            var = input("Ingrese usuario:\n→")
            if usuario1 == var:
                password = int(input("Ingrese contraseña:\n→"))
                if password == contrasena1:  # si el usuario ya existe, y se registra correctamente, vera el menu 2
                    while opcion != 3:
                        print("\tMi menu 2")
                        print("1)Llamar")
                        print("2)Enviar Correo")
                        print("3)Salir")
                        try:
                            opcion = int(input("→"))
                        except ValueError:
                            print("Debe ingresar sólo números")
                        # Aqui ponemos la seleccion del usuario del menu
                        if opcion == 1:
                            num = int(input("Ingrese telefono:\n→"))
                            while 100000000 > num or num > 999999999:
                                print("Error al ingresar el numero!")
                                num = int(input("Ingrese telefono:\n→"))
                            print(f"Llamando a {num}...")
                            input("Presione enter para continuar...")
                        if opcion == 2:
                            correo = input("Ingrese correo:\n→")
                            contador = 0  # este contador es para validar que solo hay un @
                            for i in correo:
                                if i == "@":  # contando cuantos @ escribio el usuario
                                    contador = contador + 1
                            while contador != 1:
                                print("Error, debe tener 1 y solo un @")
                                correo = input("Ingrese correo:\n→")
                                contador = 0
                                for i in correo:
                                    if i == "@":
                                        contador = contador + 1
                            mensaje = input("mensaje:\n ")
                            print(f"Enviando mensaje: \n{mensaje}\nCorreo: {correo}")
                else:
                    print("Contraseña incorrecta")
            if usuario2 == var:
                password = int(input("Ingrese contraseña:\n→"))
                if password == contrasena2:
                    print("Ingreso")
                else:
                    print("Contraseña incorrecta")
            if usuario3 == var:
                password = int(input("Ingrese contraseña:\n→"))
                if password == contrasena3:
                    print("Ingreso")
                else:
                    print("Contraseña incorrecta")
    if opcion == 2:  # Aqui recien tenemos la opcion de registro de usuario, desde aqui no puedo entrar al menu 2
        if user < 3:  # Solo puedo crear 3 usuarios
            if user == 0:
                usuario1 = input("Ingrese nombre de usuario:\n→")
            try:
                contrasena1 = int(input("Ingrese contraseña:\n→"))
                user = user + 1
            except ValueError:  # Esto valida que ingresemos solo numeros y asi no se cierra el programa
                print("Debe ser de sólo números")
        elif user == 1:
            usuario2 = input("Ingrese nombre de usuario:\n→")
            try:
                contrasena2 = int(input("Ingrese contraseña:\n→"))
                user = user + 1
            except ValueError:
                print("Debe ser de sólo números")
        elif user == 2:
            usuario3 = input("Ingrese nombre de usuario:\n→")
            try:
                contrasena3 = int(input("Ingrese contraseña:\n→"))
                user = user + 1
            except ValueError:
                print("Debe ser de sólo números")
        else:
            print("Maximo de usuarios registrados...")
