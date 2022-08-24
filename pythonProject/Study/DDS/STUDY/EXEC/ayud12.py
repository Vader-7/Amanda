# EJERCICIO 6 LISTAS
nombres = []
while True:
    nom = input("INGRESE NOMBRE:")
    if nom == "NO":
        break
    nombres.append(nom)
nombres = sorted(nombres, key=len)
nombres.pop(0)
print(nombres)
