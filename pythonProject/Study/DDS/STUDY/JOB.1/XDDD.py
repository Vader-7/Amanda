# TUTORIA DIA LUNES
# FUNCION DEL MENU
def menu():
    print("""
        CENTRO MEDICO DUOC.
        
        1.- REGISTRAR PACIENTE
        2.- ATENCION PACIENTE
        3.- CONSULTAR DATOS PACIENTES
        4.- SALIR
    """)


# FUNCIONES PARA VALIDAR CAMPOS
def valida(p_dato):
    while len(p_dato) < 3:
        print("CAMPO INGRESADO INVALIDO.")
        p_dato = input("\n-->\t")


# FUNCION PARA VALIDAR CORREO
def validaC(p_correo):
    while p_correo.count("@") == 0 or p_correo.count(".") == 0:
        print("CORREO INGRESADO INVALIDO.")
        p_correo = input("\n-->\t")


# VARIABLES
opcion = 0
cliente = []
clientes = []

while opcion != 4:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
    if opcion == 1:
        print("INGRESE RUT PACIENTE.")
        rut = int(input("\n-->\t"))
        while rut > 9999999 or rut < 4000000:
            print("RUT INGRESADO INVALIDO.")
            rut = int(input("\n-->\t"))
        nombre = input("INGRESE NOMBRE\n-->\t")
        valida(nombre)
        direccion = input("INGRESE DIRECCION\n-->\t")
        valida(direccion)
        correo = input("INGRESE CORREO\n-->\t")
        validaC(correo)

        edad = int(input("INGRESE EDAD\n-->\t"))
        while edad < 0 or edad > 110:
            print("EDAD INGRESADA INVALIDA.")
            edad = int(input("INGRESE EDAD\n-->\t"))
        cliente = [str(rut), nombre, direccion, correo, edad]
        clientes.append(cliente)
    elif opcion == 2:
        print("XD")
    elif opcion == 3:
        print("INGRESE RUT A CONSULTAR")
        rut = input("\n-->\t")
        for cls in clientes:
            if rut not in cls:
                print("RUT INGRESADO NO SE ENCUENTRA EN SISTEMA.")
            else:
                for cl in cls:
                    print(f"*\t{cl}")
    elif opcion == 4:
        print("XD")
    else:
        print("OPCION INGRESDA INVALIDA.")
