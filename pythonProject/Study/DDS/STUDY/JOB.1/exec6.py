# EJERCICIOS INFORMATICA BIOMEDICA 6
valorPan = 1800
descuentoDuro = 0.6
total = 0
totalDuro = 0
print("CUANTO PAN DURO VENDIO AL DIA.")
cant = int(input("\n-->\t"))
for i in range(cant):
    total += valorPan
totalDuro = round(total - (total*descuentoDuro))
print(f"EL VALOR DEL PAN ES:\t${valorPan}")
print(f"EL VALOR DEL PAN VENDIDO SIN DESCUENTO ES:\t${total}")
print(f"EL VALOR DEL PAN VENDIDO CON DESCUENTO ES:\t${totalDuro}")