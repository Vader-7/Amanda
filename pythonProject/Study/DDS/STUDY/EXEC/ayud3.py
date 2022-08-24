# Ejercicios con Bucles
# Ejercicio 1.
import random
import sys

x = int(input("Ingrese un numero:\n\t-->\t"))
y = 0
i = 0
while y != x:
    i += 1
    y = random.randint(0, sys.maxsize)
    print(f"#{i}\t\t{y}")
    print("")
print(f"Only takes #{i} try's")
