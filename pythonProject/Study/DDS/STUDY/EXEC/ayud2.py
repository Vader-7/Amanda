montoTotal = 0
agua = 600
azucar = 1200
aceite = 1500
arroz = 1250
print("Carrito de compra\n")
print("""
      Agua --> $600
      1. SI
      2. NO
      """)
opcion = int(input("-->"))
if opcion == 1:
    print("Ingrese la cantidad que llevara:")
    cantidad = int(input("-->"))
    montoTotal = 600 * cantidad
print("Carrito de compra\n")
print("""
      Azucar --> $1200
      1. SI
      2. NO
      """)
opcion = int(input("-->"))
if opcion == 1:
    print("Ingrese la cantidad que llevara:")
    cantidad = int(input("-->"))
    azucar = azucar * cantidad
    montoTotal = montoTotal + azucar
print("Carrito de compra\n")
print("""
      Aceite --> $1500
      1. SI
      2. NO
      """)
opcion = int(input("-->"))
if opcion == 1:
    print("Ingrese la cantidad que llevara:")
    cantidad = int(input("-->"))
    aceite = aceite * cantidad
    montoTotal = montoTotal + aceite
print("Carrito de compra\n")
print("""
      Arroz --> $1250
      1. SI
      2. NO
      """)
opcion = int(input("-->"))
if opcion == 1:
    print("Ingrese la cantidad que llevara:")
    cantidad = int(input("-->"))
    arroz = arroz * cantidad
    montoTotal = montoTotal + arroz

print("""
      ¿Pertenece usted a la tercera edad?
      1. SI
      2. NO
      """)
preferencial = int(input("-->"))
if preferencial == 1:
    descuento = montoTotal * 0.25
    montoTotal = montoTotal - descuento
    print(f"Su monto total con el descuento preferencial es: ${round(montoTotal)} ")
else:
    print(f"Su monto total es: ${montoTotal}")
print("Ingrese el pago:")
pago = int(input("-->\t$"))
vuelto = pago - montoTotal
if vuelto > 0:
    print(f"Gracias por su compra su vuelto es: ${round(vuelto)}")
elif vuelto == 0:
    print("Gracias por su compra.")
else:
    print("Dinero insuficiente, Guardias!")
