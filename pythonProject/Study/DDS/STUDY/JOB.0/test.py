asientos = [
    [1, 2, 3, 4, "XX", 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    ["XX", 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
]

# VARIABLES
indice = 0
contador = 1

for asiento in asientos:
    for a in asiento:
        print(a)
        print(contador)
        print(indice)
        indice += 1
        contador += 1
    indice = 0
