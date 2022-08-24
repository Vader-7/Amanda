u = 0
t = 1
r = 0

numero = int(input("ingresa un número entre 10 y 15 \n"))
while numero < 10 or numero > 15:
    numero = int(input("El numero ingresado no esta dentro del rango, reingrese...\n"))


print("1", end=" ")
for i in range(0, numero):
    r = u + t
    print(f"{r}", end=" ")
    u = t
    t = r
print("")
