import random

juego = []
apuesta = []
ingreso = True


def numeros():
    juego.clear()
    salir = False
    contador = 0
    while not salir:
        numero = random.randrange(1, 25)
        if numero not in juego:
            juego.append(numero)
            contador += 1
        if contador == 14:
            break


def carton():
    for i in range(1, 15):
        while True:
            while True:
                try:
                    num = int(input(f"Ingrese el {i}° número de su apuesta: "))
                    break
                except ValueError:
                    print("Ingrese sólo números!")
            if 1 <= num <= 25 and num not in apuesta:
                apuesta.append(num)
                break
            elif num < 1 or num > 25:
                print("Número no válido. Ingrese un n° del 1 al 25.")
            else:
                print("Número ya ingresado.")
                input("Presione una tecla para continuar")


def resultado():
    conteo = 0
    for seleccion in juego:
        if seleccion in apuesta:
            conteo += 1
    print(f"Cantidad de puntos obtenidos: {conteo}")


while ingreso:
    print("*****************")
    print("APUESTA DE KINO")
    print("*****************")
    numeros()
    carton()
    resultado()

    while True:
        accion = input("Desea realizar una nueva apuesta? (si/no): ")

        if accion == "si":
            juego.clear()
            numeros()
            apuesta.clear()
            carton()
            resultado()

        elif accion == "no":
            print("Fin del código")
            break
        else:
            print("Ingrese una opción válida")
            input("Presione una tecla para continuar")

# el objetivo de la actividad es que el programa pregunte los 14 números
# de la apuesta (sin que se repitan) y luego se comparen con los numeros
# generados automáticamente y saber cuántos puntos obtuvo
