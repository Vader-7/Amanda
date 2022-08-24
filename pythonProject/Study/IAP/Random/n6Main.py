import n6Fun as fn

opción = 0

while opción != 3:
    print("\n\tCalculando Área y Perímetro\n\n1) Área de un circulo\n2) Perímetro de un cuadrado\n3) Salir")

    try:
        opción = int(input("\n-> "))
    except:
        print("\n¡Debes ingresar solo números!\n")
    if opción <= 0 or opción >= 4:
        print("\n¡Numero ingresado no valido!\n")

    # OPCIÓN 1

    if opción == 1:

        var1 = int(input("\nIngrese el valor del radio del círculo:\n\n→ "))
        while var1 <= 0:
            print("\n¡Debes ingresar un valor mayor a 0!")
            var1 = int(input("\nIngrese el valor del radio del círculo:\n\n→ "))

        area = fn.calcularAREA(var1)
        resultado = area
        print(f"\nEl área de un círculo con radio {var1} es {resultado}\n")

    if opción == 2:
        var2 = int(input("\nIngrese el valor de uno de los lados del cuadrado:\n\n→ "))
        while var2 <= 0:
            print("\n¡Debes ingresar un valor mayor a 0!")
            var2 = int(input("\nIngrese el valor de uno de los lados del cuadrado:\n\n→ "))

        perimetro = fn.calcularPERIMETRO(var2)
        resultado1 = perimetro
        print(f"\nEl perímetro de un cuadrado cuyo lado vale {var2} es {resultado1}\n")

    if opción == 3:
        print("\nHa salido del sistema…")
