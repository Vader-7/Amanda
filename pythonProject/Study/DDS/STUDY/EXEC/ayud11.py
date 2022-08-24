# EJERCICIOS 4.2 LISTAS
lista = []
largo = 0
x = 0
for i in range(3):
    nombre = input("INGRESE UN NOMBRE.\n-->\t")
    lista.append(nombre)
    lan = len(nombre)
    if largo < lan:
        largo = lan
        x = i
print(lista)
print(f"EL NOMBRE MAS LARGO: \t{lista[x]}")