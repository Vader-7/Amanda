from os import system

system("clear")

vocales = 0
palabra = input("Ingrese la palabra.\n-->\t")
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1
print(vocales)
if vocales <= 2:
    print("Perdio.")
elif vocales in range(3, 5):
    print("Casi ganas.")
else:
    print("Ganaste.")
