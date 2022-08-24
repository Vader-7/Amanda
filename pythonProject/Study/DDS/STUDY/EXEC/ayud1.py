# --------------------------------------------------
# Ejercicio 3.
valorTotal = 0
print("""
        Escoge un zapato de nuestro catalogo.
        
        Recuerda que por compras sobre $40.000 
        el envio es gratis. 
    """)
print("""
      1. Zapato de Cuero -- $20.000
      2. Zapato de Goma -- $10.000
      """)
opcion = int(input("-->\t"))
if opcion == 1:
    valorZ = 20000
elif opcion == 2:
    valorZ = 10000
else:
    print("Error, opcion ingresada invalida!!")
print("Ingrese la cantidad de zapatos que requiere comprar.")
cantidad = int(input("-->\t"))
valorTotal = valorZ * cantidad
if valorTotal > 40000:
    print("El valor total de su pedido es de: ", valorTotal)
else:
    print("El valor total de su pedido mas envio es: ", valorTotal + 3000)
