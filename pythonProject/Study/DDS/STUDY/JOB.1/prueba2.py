import math
import os
import time

# EJERCICIO Tyler
"""MODIFICAR PRUEBA. 
1.- UNA VEZ INGRESADA A UNA FIGURA PREGUNTAR UNA VEZ LA INFORMACIÓN (EL RADIO EN EL CASO DEL 
CIRCULO) Y CONSTRUIR UNA FUNCION QUE CALCULE EL AREA Y EL PERIMETRO. EN EL CASO DEL CUADRADO Y DEL RECTANGULO LO 
MISMO, PREGUNTAR SOLO UNA VEZ LOS DATOS Y CONSTRUIR UNA FUNCION QUE CALCULE AREA Y PERIMETRO.
2.- RETORNAR EL RESULTADO REDONDEADO. 
3.- PARA ACCEDER AL MENU PRINCIPAL PRIMERO DEBERA INGRESAR USUARIO Y CONTRASEÑA, ESTOS DATOS DEBEN SER VALIDADOS EN 
UNA FUNCION, SI EXISTEN EN SISTEMA RETORNAR UNA CADENA DE TEXTO QUE PERMITA ACCEDER AL MENU, EN CASO DE INGRESAR 
USUARIO O CONTRASEÑA ERRONEO SOLICITAR QUE REINGRESE. """


# MENU PRINCIPAL
def menu0():
    os.system("clear")
    print("""
          - MENU -
          
        1.- CIRCULO
        2.- CUADRADO
        3.- RECTANGULO
        4.- SALIR
        """)


# MENU CIRCULO
def menu1():
    os.system("clear")
    print("""
          - MENU -
          
        1.- AREA
        2.- PERIMETRO
        3.- VUELVE AL MENU
        """)


def calculoAC(p_radio):
    p_area = math.pi * p_radio ** 2
    return round(p_area)


opcion = 0
subopcion = 0

while opcion != 4:
    menu0()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("INGRESA SOLO NUMEROS PLS.")
    if opcion == 1:
        menu1()
        while True:
            try:
                subopcion = int(input("\n-->\t"))
                break
            except ValueError:
                print("OPCION INGRESADA INVALIDA.")
        if subopcion == 1:
            print("INGRESE EL RADIO")
            radio = int(input("\n-->\t"))
            print(f"EL AREA DEL CIRCULO ES:\t{calculoAC(radio)}")
            time.sleep(3)
        elif subopcion == 2:
            print("INGRESE EL RADIO")
            radio = int(input("\n-->\t"))
            perimetro = math.pi * radio * 2
            print(f"EL PERIMETRO DEL CIRCULO ES:\t{perimetro}")
            time.sleep(3)
        elif subopcion == 3:
            print("VOLVIENDO AL MENU PRINCIPAL...")
    elif opcion == 2:
        menu1()
        while True:
            try:
                subopcion = int(input("\n-->\t"))
                break
            except ValueError:
                print("OPCION INGRESADA INVALIDA.")
        if subopcion == 1:
            print("INGRESE A")
            a = int(input("\n-->\t"))
            area = a * 4
            print(f"EL AREA DEL CUADRADO ES:\t{area}")
            time.sleep(3)
        elif subopcion == 2:
            print("INGRESE A")
            a = int(input("\n-->\t"))
            perimetro = a * 4
            print(f"EL PERIMETRO DEL CUADRADO ES:\t{perimetro}")
            time.sleep(3)
        elif subopcion == 3:
            print("VOLVIENDO AL MENU PRINCIPAL...")
    elif opcion == 3:
        menu1()
        while True:
            try:
                subopcion = int(input("\n-->\t"))
                break
            except ValueError:
                print("OPCION INGRESADA INVALIDA.")
        if subopcion == 1:
            print("INGRESE A")
            a = int(input("\n-->\t"))
            print("INGRESE A")
            b = int(input("\n-->\t"))
            area = a * b
            print(f"EL AREA DEL RECTANGULO ES:\t{area}")
            time.sleep(3)
        elif subopcion == 2:
            print("INGRESE A")
            a = int(input("\n-->\t"))
            print("INGRESE B")
            b = int(input("\n-->\t"))
            perimetro = a * 2 + b * 2
            print(f"EL PERIMETRO DEL RECTANCULO ES:\t{perimetro}")
            time.sleep(3)
        elif subopcion == 3:
            print("VOLVIENDO AL MENU PRINCIPAL...")
    elif opcion == 4:
        print("ADIOS.")
    else:
        print("OPCION INGRESADA INVALIDA.")
