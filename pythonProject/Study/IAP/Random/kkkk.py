opcion = 0
"""f = 1
x = int(input("\n\t\tIngrese su numero: "))
for i in range(x):
    f *= (x - i)
    print(f'{x} x {x - i}\t\t  {f}')"""


def sumar(var1, var2):
    var3 = var1 + var2
    return var3


resultado = sumar(7, 5)
print(f"resultado: {resultado}")


def sumar(var1, var2):
    print(var1 + var2)


sumar(7, 5)


def sumar(var1, var2):
    var3 = var1 + var2
    return var3


def restar(var1, var2):
    var3 = var1 - var2
    return var3


def multiplicacion(var1, var2):
    var3 = var1 * var2
    return var3


def dividir(var1, var2):
    var3 = var1 / var2
    return var3


while opcion != 4:
    print("\t\tCalculadora")
    print("\n\t(1)\tSumar.")
    print("\t(2)\tRestar.")
    print("\t(3)\tMultiplicar.")
    print("\t(4)\tDividir.")
    print("\t(5)\tSalir.")
    try:
        opcion = int(input("\t→\t"))
    except:
        print("\t\tOpción Ingresada Invalida, digite un numero.")
    if opcion == 1:
        n1 = int(input("Ingrese el primero numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        resultado = sumar(n1, n2)
        print(f"Resultado: {resultado}")
    if opcion == 2:
        n1 = int(input("Ingrese el primero numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        resultado = restar(n1, n2)
        print(f"Resultado: {resultado}")
    if opcion == 3:
        n1 = int(input("Ingrese el primero numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        resultado = multiplicacion(n1, n2)
        print(f"Resultado: {resultado}")
    if opcion == 4:
        n1 = int(input("Ingrese el primero numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        resultado = dividir(n1, n2)
        print(f"Resultado: {resultado}")
    if opcion == 5:
        print("\n\t\tHa salido del sistema....\n\t\tHASTA PRONTO.")
        break
