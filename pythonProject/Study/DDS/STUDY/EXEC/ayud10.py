# EJERCICIOS 3 LISTAS
# VARIABLES
lista = []
total = 0
# INGRESAMOS NUMEROS A NUESTRA LISTA.
for i in range(10):
    numero = int(input(f"{i + 1}.\n-->\t"))
    lista.append(numero)
# COMPROBAMOS DATOS EN LISTA
print("\n")
print(lista)
# SUMAMOS ELEMENTOS DE LA LISTA
for i in range(len(lista)):
    total += lista[i]
# CALCULAMOS PROMEDIO
promedio = total / len(lista)
# IMPRIMIMOS PROMEDIO
print(f"\nEL PROMEDIO ES: %{promedio}")
