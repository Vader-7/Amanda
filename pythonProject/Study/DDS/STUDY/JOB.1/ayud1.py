# AYUDANTIA INFORMATICA BIOMEDICA 1
contador = 0
contador1 = 0
nombre = input("\n-->\t")
while not nombre.isalpha() or len(nombre) < 3:
    print("NOMBRE INGRESADO INVALIDO")
    nombre = input("\n-->\t")

nombre = input("\n-->\t")
while nombre[0].isupper():
    print("NOMBRE INGRESADO INVALIDO")
    nombre = input("\n-->\t")
nombre = "HOLA"

for char in nombre:
    if "@" in char:
        contador += 1
    elif "." in char:
        contador1 += 1
    else:
        contador = 0

suma = 0
promedio = 0.0
print("INGRESE LA CANTIDAD DE NOTAS.")
cant = int(input("\n-->\t"))
for i in range(cant):
    print(f"INGRESE LA {i + 1} NOTA.")
    nota = int(input("\n-->\t"))
    suma += nota
promedio = suma/cant
print(f"EL PROMEDIO ES:\t{promedio}")
