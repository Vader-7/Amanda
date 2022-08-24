from os import system

system("clear")

# 1.
while True:
    try:
        a = int(input("Ingrese A:\n\t-->\t"))
        b = int(input("Ingrese B:\n\t-->\t"))
        c = a / b
        # if c <= 0:
        # raise Exception("Error en la division")
        print(f"El resultado es: {round(c)}")
        break
    except ZeroDivisionError:
        print("\nERROR!! \nESTAS DIVIDIENDO x 0.\n")
    except ValueError:
        print("\nERROR!! \nESTAS INGRESANDO LETRAS.\n")
