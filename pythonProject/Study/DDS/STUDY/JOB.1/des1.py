# DESAFIO
def menu():
    print("""
        1.- CALCULAR PROMEDIO.
        2.- SALIR.
        """)


# VARIABLES
opcion = 0
suma = 0
promedio = 0
user = "profe"
pasw = "123"


while opcion != 2:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
    if opcion == 1:
        print("INGRESE USUARIO.")
        usuario = input("\n-->\t")
        print("INGRESE CONTRASEÑA.")
        contra = input("\n-->\t")
        if contra != pasw or usuario != user:
            print("USUARIO O CONTRASEÑA INVALIDA.")
        else:
            print("INGRESE EL NOMBRE DEL ALUMNO.")
            alumno = input("\n-->\t")
            print(f"INGRESE LA CANTIDAD DEL ALUMNO: {alumno}")
            cant = int(input("\n-->\t"))
            for i in range(cant):
                print(f"INGRESE LA {i + 1} NOTA.")
                nota = int(input("\n-->\t"))
                suma += nota
            promedio = suma/cant
            print(f"EL ALUMNO {alumno} TIENE UN PROMEDIO:\t{promedio}")
    elif opcion == 2:
        print("ADIOS.")
    else:
        print("OPCION INGRESADA INVALIDA.")