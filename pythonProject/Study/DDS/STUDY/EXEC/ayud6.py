# EJERCICIO 2 LISTAS
print("INGRESE TAMAÑO LISTA.")
tam = int(input("\n-->\t"))
lista = []
for i in range(tam):
    numero = int(input(f"{i + 1}\n-->\t"))
    if numero == 0:
        print("DATO INVALIDO EN LA LISTA.")
        break
    else:
        lista.append(numero)
lista.sort()
print(lista)
