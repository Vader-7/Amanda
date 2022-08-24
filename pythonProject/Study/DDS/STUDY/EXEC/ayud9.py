# EJERCICIOS 5 LISTAS
lista0 = ['Tyler', 'Nicolas', 'Maximiliano']
lista1 = ['Diaz', 'Hayashi', 'Momo']
lista2 = []
for i in range(3):
    lista2.append(lista0[i])
    lista2[i] = lista2[i] + " " + lista1[i]

print(lista2)
