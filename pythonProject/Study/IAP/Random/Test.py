palomitas = 0
bebidas = 0
total = 0


def menu():
    print("\t\tBienvenido a CineDuoc")
    print("\t[1] Si usted pertenece a la Institucion.")
    print("\t[2] Si usted no pertenece a la Institucion.")
    print("\t[0] Si usted desea salir del menu.")


menu()
option = int(input("Ingrese su opcion: "))

while option != 0:
    if option == 1:
        registro = input("Ingrese su indentificacion: ")
        print("\t\tQue tipo de entrada usted desea\n\t[1] Estreno $4.800\n\t[2] Normal $2.900")
        optione = int(input("Ingrese su opcion: "))
        if optione == 1:
            total = 4800 - (4800 * 0.30)
        if optione == 2:
            total = 2900 - (2900 * 0.30)
        print(f"El valor de su entrada con el descuento por ser parte de la Institucion DUOC es: ${round(total)}")
        opcionC = input("\tDesea agregar palomitas de Maiz? (Si o No) ")
        if opcionC == "Si":
            print("\t[1] Palomitas Pequeñas $2.500\n\t[2] Palomitas Medianas $4.500\n\t[3] Palomitas Grandes $7.800")
            optionp = int(input("Ingrese su opcion: "))
            if optionp == 1:
                r = int(input("Cuantas desea? "))
                palomitas = (2500 * r)

            if optionp == 2:
                r = int(input("Cuantas desea? "))
                palomitas = (4500 * r)

            if optionp == 3:
                r = int(input("Cuantas desea? "))
                palomitas = (7800 * r)
            else:
                print("Opcion Invalida.")

            optionB = input("\tDesea agregar una Bebida? (Si o No) ")
            if optionB == "Si":
                print("\t[1] Bebidas pequeñas $1.000\n\t[2] Bebidas medianas $1.250\n\t[3] Bebidas grandes $2.000")
                optionb = int(input("Ingrese su opcion: "))
                if optionb == 1:
                    r = int(input("Cuantas desea? "))
                    bebidas = (1000 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

                if optionb == 2:
                    r = int(input("Cuantas desea? "))
                    bebidas = (1250 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

                if optionb == 3:
                    r = int(input("Cuantas desea? "))
                    bebidas = (2000 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")
                else:
                    print("Opcion Invalida.")
            else:
                print(f"El total a pagar es: ${round(total + palomitas)}")
                total = (palomitas + total)
                pago = int(input("Ingrese con cuanto dinero cancela: "))
                vuelto = (pago - total)
                if vuelto < 0:
                    print("Le falta dinero.")
                else:
                    print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

        else:
            print(f"\n\tEl total a pagar es: ${round(total)}")
            pago = int(input("Ingrese con cuanto dinero cancela: "))
            vuelto = (pago - total)
            if vuelto < 0:
                print("Le falta dinero.")
            else:
                print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

    if option == 2:
        print("\t\tQue tipo de entrada usted desea\n\t[1] Estreno $4.800\n\t[2] Normal $2.900")
        optione = int(input("Ingrese su opcion: "))
        while optione > 2 or optione <= 0:
            optione = int(input("\n\t\tOpcion Ingresada Invalida!.\n\t\tIngrese su opcion: "))
        if optione == 1:
            total = 4800
        else:
            total = 2900
        opcionC = input("\tDesea agregar palomitas de Maiz? (Si o No) ")
        if opcionC == "Si":
            print("\t[1] Palomitas Pequeñas $2.500\n\t[2] Palomitas Medianas $4.500\n\t[3] Palomitas Grandes $7.800")
            optionp = int(input("Ingrese su opcion: "))
            if optionp == 1:
                r = int(input("Cuantas desea? "))
                palomitas = (2500 * r)

            if optionp == 2:
                r = int(input("Cuantas desea? "))
                palomitas = (4500 * r)

            if optionp == 3:
                r = int(input("Cuantas desea? "))
                palomitas = (7800 * r)

            optionB = input("\tDesea agregar una Bebida? (Si o No) ")
            if optionB == "Si":
                print("\t[1] Bebidas pequeñas $1.000\n\t[2] Bebidas medianas $1.250\n\t[3] Bebidas grandes $2.000")
                optionb = int(input("Ingrese su opcion: "))
                if optionb == 1:
                    r = int(input("Cuantas desea? "))
                    bebidas = (1000 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

                if optionb == 2:
                    r = int(input("Cuantas desea? "))
                    bebidas = (1250 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

                if optionb == 3:
                    r = int(input("Cuantas desea? "))
                    bebidas = (2000 * r)
                    print(f"El total a pagar es: ${round(total + bebidas + palomitas)}")
                    total = (palomitas + bebidas + total)
                    pago = int(input("Ingrese con cuanto dinero cancela: "))
                    vuelto = (pago - total)
                    if vuelto < 0:
                        print("Le falta dinero.")
                    else:
                        print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")

            else:
                print(f"El total a pagar es: ${round(total + palomitas)}")
                total = (palomitas + total)
                pago = int(input("Ingrese con cuanto dinero cancela: "))
                vuelto = (pago - total)
                if vuelto < 0:
                    print("Le falta dinero.")
                else:
                    print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")
        else:
            print(f"\n\tEl total a pagar es: ${round(total)}")
            pago = int(input("Ingrese con cuanto dinero cancela: "))
            vuelto = (pago - total)
            if vuelto < 0:
                print("Le falta dinero.")
            else:
                print(f"Su vuelto es: ${round(vuelto)}\n\tHasta Pronto.")
    else:
        break
print("\n\n\t\tHasta Pronto.\n\n")
