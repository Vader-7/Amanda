import random

"""
juego = []
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
            break"""

# el objetivo de la actividad es que el programa pregunte los 14 números
# de la apuesta (sin que se repitan) y luego se comparen con los numeros
# generados automáticamente y saber cuántos puntos obtuvo


numeros = []
a = []


def numero(p_numero):
    for i in range(p_numero):
        x = int(input("\n-->\t"))
        while x in a:
            print("Número repetido.")
            x = int(input("\n-->\t"))
        numeros.append(x)
        a.append(x)
    return numeros


def bingo(p_numeros):
    for i in p_numeros:
        if i == random.randint(0, 100):
            print("BINGO!")
        else:
            print("F")


print("Ingrese la cantidad de números.")
cant = int(input("\n-->\t"))
bingo(numero(cant))
