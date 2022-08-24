# lista productos
productos = [
    ["Nombre1", 300, 0],
    ["Nombre2", 500, 0],
    ["Nombre3", 400, 0]
]
print("1.")
# como recorrer la lista
for prod in productos:
    print(prod)

print("\n2.")
# como filtrar la lista, ejemplo.
for prod in productos:
    # la posicion 1 del recorrido es el precio, lo usaremos como condición
    if prod[1] == 500:
        print(prod)

print("\n3.")
# ejemplo como calcular promedio de una lista
# la posicion 2 es el precio
precios = [prod[1] for prod in productos]
print(precios)
# promedio
print(sum(precios) / len(precios))
# ejemplo como calcular promedio de una lista 2
suma = 0
for prod in productos:
    # suma iniciara en 0 y se sumara el precio en cada iteracion
    suma += prod[1]
promedio = suma / len(productos)
print(promedio)
