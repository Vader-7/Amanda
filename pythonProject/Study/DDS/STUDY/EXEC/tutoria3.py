from os import system

system("clear")

# VARIABLES
opcion = 0
user1 = None
user2 = None
user3 = None
pass1 = None
pass2 = None
pass3 = None
celular = None
arroba = None
valida = 0
# ALGORITMO
# MENU
while opcion != 3:
    print("""
            1.  INICIAR SESIÓN.
            2.  REGISTRO USUARIO.
            3.  SALIR.
            """)
    opcion = int(input("\n-->\t"))
    if opcion == 1:
        while opcion != 0:
            print("INGRESE SU USUARIO.")
            user = input("\n-->\t")
            print("INGRESE SU CONTRASEÑA.")
            passw = input("\n-->\t")
            if user1 == user and passw == pass1 or user2 == user and pass2 == passw or user3 == user and pass3 == passw:
                while True:
                    print("""
                            1. REALIZAR LLAMADA.
                            2. ENVIAR CORREO ELECTRÓNICO.
                            3. CERRAR SESIÓN.
                            """)
                    opcion = int(input("\n-->\t"))
                    if opcion == 1:
                        print("INGRESE SU CELULAR EJEMPLO(98544756).")
                        while True:
                            try:
                                celular = input("\n-->\t")
                                break
                            except ValueError:
                                print("FORMATO INGRESADO INVALIDO")
                        for nueve in celular:
                            if nueve[0] != 9 and len(celular) < 8:
                                print("FORMATO INGRESADO INVALIDO")
                                break
                            else:
                                celular = celular
                                print("CELULAR REGISTRADO")
                                break
                        valida += 1
                    if opcion == 2:
                        print("INGRESE SU CORREO.")
                        var_correo = input("\n-->\t")
                        contador = 0
                        for i in var_correo:
                            if i == "@":
                                print("CORREO ENVIADO.")
                                correo = var_correo
                                contador = contador + 1
                        while contador != 1:
                            print("CORREO INVALIDO, INGRESE SU CORREO.")
                            correo = input("\n-->\t")
                            contador = 0
                            for i in correo:
                                if i == "@":
                                    print("CORREO ENVIADO.")
                                    correo = var_correo
                                    contador = contador + 1
                            valida += 1
                    if opcion == 3:
                        print("SESIÓN CERRADA.")
                        break
                opcion = 0
            else:
                print("ES NECESARIO REGISTRAR USUARIO.")
                opcion = 0
    if opcion == 2:
        if user1 is None:
            print("INGRESE SU NOMBRE DE USUARIO.")
            user = input("\n-->\t")
            user1 = user
            print("INGRESE SU CONTRASEÑA.")
            passw = input("\n-->\t")
            pass1 = passw
        elif user2 is None:
            print("INGRESE SU NOMBRE DE USUARIO.")
            user = input("\n-->\t")
            user2 = user
            print("INGRESE SU CONTRASEÑA.")
            passw = input("\n-->\t")
            pass2 = passw
        elif user3 is None:
            print("INGRESE SU NOMBRE DE USUARIO.")
            user = input("\n-->\t")
            user3 = user
            print("INGRESE SU CONTRASEÑA.")
            passw = input("\n-->\t")
            pass3 = passw
        else:
            print("LIMITE DE USUARIOS ALCANZADOS.")
    if opcion == 3:
        print("\n\tADIOS.")
