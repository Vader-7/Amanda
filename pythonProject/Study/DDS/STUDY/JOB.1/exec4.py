# EJERCICIOS INFORMATICA BIOMEDICA 4
print("INGRESE UN NUMERO.")
num = int(input("\n-->\t"))
fac = 1
cont = 1
for i in range(num):
    fac = fac * cont
    cont += 1
print(f"\nEL FACTORIAL DE {num} ES:\t{fac}")
