from os import system

system("clear")

suma = 1
numero = int(input("Ingrese su numero:\n-->\t"))
for i in range(1, numero, 2):
    print(suma)
    suma = suma + 2
print("\n", suma)
