# EJERCICIO 4 LISTAS
lista = []
for i in range(3):
    print(f"INGRESE EL {i + 1} NOMBRE")
    nombre = input("\n-->\t")
    lista.append(nombre)

"""for i in reversed(sorted(lista, key=len)):
    print(lista)"""

lista = sorted(lista, key=len, reverse=True)
print(lista[0])


