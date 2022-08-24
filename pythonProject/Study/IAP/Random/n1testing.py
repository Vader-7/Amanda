
#pop
asientos = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
]

"""asientos = numpy.array([None] * 7)
for i in range(7):
    asientos[i] = ([None] * 6)"""
# print(asientos.shape)

opción = 0
tipo = 0
descuento = 0.15
val = 0
val2 = 0
compra = 0
banco = 0
valorBoleto = 0
rutPasajero = 0
telefonoPasajero = 0
bancoPasajero = 0
nombrePasajero = None
asientoP = 0

while opción != 5:
    print("1.\tVer asientos disponibles:")
    print("2.\tComprar asientos:")
    print("3.\tAnular vuelo:")
    print("4.\tModificar datos de pasajero:")
    print("5.\tSalir.")
    try:
        opción = int(input("\t->\t"))
    except:
        print("\t\tOpción Ingresada Invalida, ingrese un numero.")
    if opción == 1:
        print("\n")
        for i in range(7):
            print("|")
            for j in range(6):
                if j == 3:
                    print("\t\t", asientos[i][j], end="")
                else:
                    print("\t",asientos[i][j], end="")
            if i == 4:
                print("\n")
                print("-" * 60)
                print("-" * 60)
            print("|")
    if opción == 2:
        nombrePasajero = input("Ingrese su nombre: ")
        telefonoPasajero = int(input("Ingrese su telefono: "))
        rutPasajero = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->\t"))
        while rutPasajero < 5000000 or rutPasajero > 999999999:
            print("\t\tRUT INVALIDO")
            rutPasajero = int(input("\tIngrese su RUT, solo números sin guión ni coma.\n\t->\t"))
        print("\n")
        for i in range(7):
            print("|")
            for j in range(6):
                if j == 3:
                    print("\t\t", asientos[i][j], end="")
                else:
                    print("\t",asientos[i][j], end="")
            if i == 4:
                print("\n")
                print("-" * 60)
                print("-" * 60)
            print("|")
        asiento = int(input("Ingrese el numero de asiento que desea: \n\t(1-30) Normal.\n\t(31-42) Vip.\n\t->\t"))
        asientoP = asiento
        if asiento >= 31:
            for i in range(7):
                for j in range(6):
                        if asientos[i][j] == asiento:
                            asientos[i][j] = 'x'
                            valorBoleto = 240000
                            while tipo == 0:
                                banco = int(input("Usted es miembro de Banco DUOC? 1) SI - 2) NO:\n\t->\t"))
                                if banco == 1:
                                    des = valorBoleto * descuento
                                    valorBoleto -= des
                                    print(f"El valor de su boleto con el descuento por pertenecer a Banco DUOC es: $",round(valorBoleto))
                                    tipo = tipo + 1
                                if banco == 2:
                                    print(f"El valor de su boleto es de: ${valorBoleto}")
                                    tipo = tipo + 1
                        else:
                            print("Asiento no disponible.")
        else:
            for i in range(7):
                for j in range(6):
                        if asientos[i][j] == asiento:
                            asientos[i][j] = 'x' 
                            valorBoleto = 78900
                            while tipo == 0:
                                banco = int(input("Usted es miembro de Banco DUOC? 1) SI - 2) NO:\n\t->\t"))
                                if banco == 1:
                                    des = valorBoleto * descuento
                                    valorBoleto -= des
                                    print(f"El valor de su boleto con el descuento por pertenecer a Banco DUOC es: $",round(valorBoleto))
                                    tipo = tipo + 1
                                if banco == 2:
                                    print(f"El valor de su boleto es de: ${valorBoleto}")
                                    tipo = tipo + 1
                        else:
                            print("Asiento no disponible.")
    if opción == 3:
        val = 0
        while val == 0:
            val = int(input("Ingrese si quiere anular su boleto 1) SI 2) NO\n\t->\t"))
            if val == 1:
                
                val = val + 1
            if val == 2:
                val = val + 1
    if opción == 4:
        asiento = int(input("Ingrese su numero de asiento:\n\t->\t"))
        if asiento == asientoP:
            rut = int(input("Ingrese su RUT: "))
            if rut == rutPasajero:
                while val2 != 3:
                    print("1.\tModificar su nombre.")
                    print("2.\tModificar su telefono.")
                    print("3.\tSALIR.\n")
                    try:
                        val2 = int(input("\t->\t"))
                    except:
                        print("\t\tOpción Ingresada Invalida, ingrese un numero.")
                    if val2 == 1:
                        nombreN = input("Ingrese el nuevo nombre: ")
                        nombrePasajero = nombreN
                    if val2 == 2:
                        teleN = int(input("Ingrese el nuevo numero de telefono: "))
                        telefonoPasajero = teleN
                    else:
                        print("\n\tOpción ingresada Invalida.")
            else:
                print("Rut no registrado.")        
        else:
                print("Asiento no registrado.")
    if opción == 5:
        print("\n\t\tHa salido del sistema....\n\t\tHASTA PRONTO.")
        break