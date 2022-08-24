from os import system
system("clear")

vocal = 0
palabra = input("Ingrese la palabra:\n-->\t")
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocal += 1
print(vocal)
if vocal <= 2:
    print("Perdiste.")
elif 3 <= vocal <= 5:
    print("Casi ganas.")
else:
    print("GANASTE!!")