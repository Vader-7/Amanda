# AYUDANTIA INFORMATICA BIOMEDICA 2
import math


# FUNCION MENU
def menu():
    print("""
        1.- CIRCULO.
        2.- CUADRADO.
        3.- RECTANGULO.
        4.- SALIR.
        """)


def menuCuadrado():
    print("""
            CUADRADO
            1.- AREA.
            2.- PERIMETRO.
            """)


def menuCirculo():
    print("""
            CIRCULO
            1.- AREA.
            2.- PERIMETRO.
            """)


def menuRectangulo():
    print("""
            RECTANGULO
            1.- AREA.
            2.- PERIMETRO.
            """)


# VARIABLES
opcion = 0
in_opcion = 0

# MENU
while True:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
    if opcion == 1:
        menuCirculo()
        try:
            in_opcion = int(input("\n-->\t"))
        except ValueError:
            print("OPCION INGRESADA INVALIDA.")
        if in_opcion == 1:
            print("INGRESE PERIMETRO.")
            radio = int(input("\n-->\t"))
            area = math.pi * radio ** 2
            print(f"EL AREA DEL CIRCULO ES:\t{area}")
        elif in_opcion == 2:
            print("INGRESE EL RADIO.")
            radio = int(input("\n-->\t"))
            perimetro = (math.pi * 2) * radio
            print(f"EL PERIMETRO DEL CIRCULO ES:\t{perimetro}")
        else:
            print("OPCION INGRESADA INVALIDA.")
    elif opcion == 2:
        menuCuadrado()
        in_opcion = int(input("\n-->\t"))
        if in_opcion == 1:
            print("INGRESE X.")
            largo = int(input("\n-->\t"))
            area = largo ** 2
            print(f"EL AREA DEL CUADRADO ES:\t{area}")
        elif in_opcion == 2:
            print("INGRESE X.")
            largo = int(input("\n-->\t"))
            perimetro = largo ** 2
            print(f"EL PERIMETRO DEL CUADRADO ES:\t{perimetro}")
        else:
            print("OPCION INGRESADA INVALIDA")
    elif opcion == 3:
        menuRectangulo()
        in_opcion = int(input("\n-->\t"))
        if in_opcion == 1:
            print("INGRESE X.")
            x = int(input("\n-->\t"))
            print("INGRESE Y.")
            y = int(input("\n-->\t"))
            area = x * y
            print(f"EL AREA DEL CUADRADO ES:\t{area}")
        elif in_opcion == 2:
            print("INGRESE X.")
            x = int(input("\n-->\t"))
            print("INGRESE Y.")
            y = int(input("\n-->\t"))
            perimetro = x * 2 + y * 2
            print(f"EL PERIMETRO DEL CUADRADO ES:\t{perimetro}")
        else:
            print("OPCION INGRESADA INVALIDA")
    elif opcion == 4:
        print("ADIOS.")
        break
    else:
        print("OPCION INGRESADA INVALIDA")
