# LISTAS
lista = []
print(type(lista))

nombre = "Henry"
lista = ["Mario", "María", "Gerald", "Tyler", "Javier", nombre]
print(lista)
lista.append("Wacoldo")
print(lista)

for elem in lista:
    print(elem)

print("\n" + lista[4])
lista.append("Diogenes")
lista.insert(0, True)
lista.remove("Henry")
lista.remove(lista[0])
lista.insert(0, "Rudeos")
print(lista)
print(len(lista))
print(lista.count("Gerald"))
lista.clear()
print(lista)

lista2 = lista.copy()
print(lista2)
