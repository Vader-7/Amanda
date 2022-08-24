#EJERCICIO 1.
vocales = 0
consonantes = 0
for i in range(10):
    print("Ingrese la letra", i + 1)
    letra = input("-->")
    if letra =="a" or letra == "e" or letra == "i" or letra =="o" or letra == "u":
         vocales = vocales + 1   
    else:
        consonantes = consonantes + 1
                    
print("La cantidad de vocales es:", vocales)
print("La cantidad de consonantes es:", consonantes)
#EJERCICIO 2.
numMayor = 0
numMenor = 0
numIgual = 0
for i in range(5):
    print("Ingrese el", i + 1 + " numero.")
    numero = int(input("-->\t"))
    if numero > 0:
        numMayor = numMayor + 1
    elif numero == 0:
        numIgual = numIgual + 1
    else:
        numMenor =  numMenor + 1
print("La cantidad de numeros mayores a 0 es:", numMayor)
print("La cantidad de numeros iguales a 0 es:", numIgual)
print("La cantidad de numeros menores a 0 es:", numMenor)