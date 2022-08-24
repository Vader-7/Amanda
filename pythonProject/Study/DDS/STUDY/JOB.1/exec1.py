# EJERCICIOS INFORMATICA BIOMEDICA 1
import os 
os.system("clear")

print("INGRESE UN NUMERO ENTERO")
numero = int(input("\n-->\t"))
total = 0
for i in range(numero):
    i += 1
    print(i)
    total = i
print(f"\nEL TOTAL ES:\t{total}")

