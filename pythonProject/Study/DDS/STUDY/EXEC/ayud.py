# Ejercicios ayudantias Python
# Ejercicio 1.
print("¿Cual de los siguientes animales vive en el agua?")
print("""
      Eliga una opcion
      1. Perro
      2. Cocodrilo 
      3. Conejo
      4. Tiburon\n\t-->\t""")
opcion = int(input())
puntaje = 0.0
if opcion == 2:
    puntaje = 0, 5
elif opcion == 4:
    puntaje = 1, 0
else:
    puntaje = 0

print("El puntaje obtenido es:", puntaje)
# --------------------------------------------------
# Ejercicio 2.
miembro = False
valorTotal = 0
print("BIENVENIDO A CINEDUOC")
print("""¿Pertenece usted a DUOC? (Estudiante/Funcionario).
        1.  SI
        2.  NO\n->\t""")
mOpcion = int(input())
if mOpcion == 1:
    miembro = True
elif mOpcion == 2:
    miembro = False
else:
    print("Error, opcion invalida!!")
print("""Las entradas que se encuentran disponibles son:
        1. ESTRENO --> $4.800
        2. NORMAL --> $2.900""")
eOpcion = int(input())
if eOpcion == 1:
    if miembro:
        valorEntrada = (4800 * 0.30)
    else:
        valorEntrada = 4800
elif eOpcion == 2:
    if miembro:
        valorEntrada = (2900 * 0.30)
    else:
        valorEntrada = 2900
else:
    print("Error, opcion invalida!!")
print("¿Cuantas entradas desea comprar?\n->")
cantidadE = int(input())
valorEntrada = valorEntrada * cantidadE
valorTotal = valorTotal + valorEntrada
print("""
      ¿Desea agregar palomitas de maíz?
      
    ESCRIBA POR TECLADO LA OPCION QUE DESEA(SI/NO)
      """)
ePalomitas = input()
if ePalomitas == "SI":
    print("""
          Promociones:
          1. Palomita pequeña --> $2.500
          2. Palomita mediana --> $4.500
          3. Palomita grande --> $7.800
          """)
    pOpcion = int(input())
    if pOpcion == 1:
        valorPalomita = 2500
    elif pOpcion == 2:
        valorPalomita = 4500
    elif pOpcion == 3:
        valorPalomita = 7800
    else:
        print("Error, opcion invalida!!")
    print("¿Cuantas promociones desea comprar?\n->")
    cantidadP = int(input())
    valorPalomita = valorPalomita * cantidadP
    valorTotal = valorTotal + valorPalomita
print("""
      ¿Desea agregar bebidas?
      
    ESCRIBA POR TECLADO LA OPCION QUE DESEA(SI/NO)
      """)
ePalomitas = input()
if ePalomitas == "SI":
    print("""
          Promociones:
          1. Bebida pequeña --> $1.000
          2. Bebida mediana --> $1.250
          3. Bebida grande --> $2.000
          """)
    bOpcion = int(input())
    if bOpcion == 1:
        valorBebida = 1000
    elif bOpcion == 2:
        valorBebida = 1250
    elif bOpcion == 3:
        valorBebida = 2000
    else:
        print("Error, opcion invalida!!")
    print("¿Cuantas bebidas desea comprar?\n->")
    cantidadB = int(input())
    valorBebida = valorBebida * cantidadB
    valorTotal = valorTotal + valorBebida

print("El total a pagar es: ", round(valorTotal))
pago = int(input("Ingrese con cuanto cacela:\n\t->"))
vuelto = round(pago - valorTotal)
if vuelto > 0:
    print(f"Su vuelto es: $ {vuelto} .\nGracias por su compra!!")
elif vuelto == 0:
    print("Gracias por su compra!!")
else:
    print("Pago insuficiente.\t:(")
