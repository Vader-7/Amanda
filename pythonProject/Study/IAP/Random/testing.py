import numpy

opción = 0
a = 0

asientos = numpy.array([None] * 7)
for i in range(7):
    asientos[i] = ([None] * 6)

# print(asientos.shape)

while opción != 2:
    print("1)\tPara comprobar si existe asiento disponible.")
    print("2)\tSalir.")
    try:
        opción = int(input("\t->\t"))
    except:
        print("\t\tOpción ingresada invalida, ingrese un numero.")
    for i in range(7):
        for j in range(6):
            if j == 3:
                print("\t", asientos[i][j], end=" ")
            else:
                print(asientos[i][j], end=" ")
        print("")
    if opción == 1:
        for i in range(7):
            for j in range(6):
                if asientos[i][j] == asientos[0][j]:
                    a = a + 1
        asiento = int(input("Ingrese numero de asiento que desea consultar: "))
        for i in range(7):
            for j in range(6):
                if asientos[i][j] == None:

                    print("Asiento disponible, Registro realizado con éxito.")

                else:
                    print("Asiento ocupado.")
    else:
        print("Bye")

for i in range(7):
    for j in range(6):
        if j == 3:
            print("\t", asientos[i][j], end=" ")
        else:
            print(asientos[i][j], end=" ")
    print("")
