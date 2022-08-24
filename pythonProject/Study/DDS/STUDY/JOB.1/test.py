lista = [["20", "Lechuga", "700"], ["30", "Palta", "7000"]]

id = input("-->")
for prod in lista:
    if id in prod:
        print("""
        1.- Nombre
        2.- Precio
        """)
        opcion = int(input("-->"))
        prod[opcion] = input("-->")

print(lista)