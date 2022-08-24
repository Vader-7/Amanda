# VALIDA NOMBRE
nombre = input("\n-->\t")
while not nombre.isalpha():
    print("NOMBRE INGRESADO INVALIDO.")
    nombre = input("\n-->\t")

nombre = "TYLER"
for char in nombre:
    if char == "T":
        print("XD")