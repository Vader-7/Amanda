# EJERCICIO 3 LISTAS
print("INGRESE EL TAMAÑO DE SU LISTA.")
tam = int(input("\n-->\t"))
lista = []
total = 0
promedio = 0
for i in range(tam):
    print(f"INGRESE EL {i + 1} NUMERO.")
    num = int(input("\n-->\t"))
    lista.append(num)
print(lista)
for elem in lista:
    total += elem

promedio = round(total / len(lista))
print("LA SUMA DE SU LISTA ES:", total)
print("EL PROMEDIO DE SU LISTA ES:", promedio)
