descuento = 10  # descuento del caso es del 20%
print("Ingrese monto a pagar.")
monto = int(input("\n-->\t"))
print(f"El monto a pagar es:\t${monto}")
print("Aplicando descuento...")
descuento = (descuento * monto)/100
monto = monto - descuento
print(f"El monto a pagar es:\t${round(monto)}")
