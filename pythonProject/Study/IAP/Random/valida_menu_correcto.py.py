opcion = 0

user = 0
usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None
while (opcion != 3):
    print("\tMi menu")
    print ("1)Iniciar sesión")
    print ("2)Registrar usuarios")
    print ("3)Salir")
    try:
        opcion = int(input("→"))
    except:
        print("Debe ingresar sólo números")
    if(opcion == 1):
        if (user == 0):
            print("Debe crear un usuario primero")
        else:
            var = input("ingrese usuario →")
            if (usuario1 == var):
                password = int(input("ingrese contraseña→"))
                if (password == contrasena1):
                    while (opcion != 3):
                        print("\tMi menu 2")
                        print ("1)Llamar")
                        print ("2)Enviar Correo")
                        print ("3)Salir")
                        try:
                            opcion = int(input("→"))
                        except:
                            print("Debe ingresar sólo números")

                        if (opcion == 1):
                            num = int (input("ingrese telefono→"))
                            while(10000000 > num or num > 99999999):
                                print ("error al ingresar numero !")
                                num = int (input("ingrese telefono→"))
                            print (f"Llamando a  {num}...")
                            input("Presione enter para continuar...")    
                        if (opcion == 2):
                            correo = input("ingrese correo→")
                            contador = 0
                            for i in correo:
                                if (i == "@"):
                                    contador = contador +1
                            while (contador != 1 ):
                                print ("error , debe tener 1 y sólo un @")
                                correo = input("ingrese correo→")
                                contador = 0
                                for i in correo:
                                    if (i == "@"):
                                        contador = contador +1
                            mensaje = input("mensaje:")
                            print (f"Enviando mensaje :\n{mensaje}\nCorreo : {correo}")
                else:
                    print ("contraseña incorrecta")
            if (usuario2 == var):
                password = int(input("ingrese contraseña→"))
                if (password == contrasena2):
                    print ("ingreso")
                else:
                    print ("contraseña incorrecta")
            if (usuario3 == var):
                password = int(input("ingrese contraseña→"))
                if (password == contrasena3):
                    print ("ingreso")
                else:
                    print ("contraseña incorrecta")
    if(opcion == 2):
        if (user <3):
            if (user == 0):
                usuario1 = input("Ingrese nombre usuario →")
                try:
                    contrasena1 = int(input("ingrese contraseña →"))
                    user = user +1
                except:
                    print ("Debe ser sólo número")
            elif(user == 1):
                usuario2 = input("Ingrese nombre usuario →")
                try:
                    contrasena2 = int(input("ingrese contraseña →"))
                    user = user +1
                except:
                    print ("Debe ser sólo número")
            elif (user == 2):
                usuario3 = input("Ingrese nombre usuario →")
                try:
                    contrasena3 = int(input("ingrese contraseña →"))
                    user = user +1
                except:
                    print ("Debe ser sólo número")
        else:
            print ("Maximo de usuarios registrados...")