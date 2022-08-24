x = int(input("Ingrese un numero entero:\n\n→ "))
while (x <= 0):
    print ("\n¡Debes ingresar un valor mayor a 0!")
    x = int(input("\nIngrese un numero entero:\n\n→ ")) 

y = int(input("\nIngrese otro numero entero:\n\n→ "))
while (y <= 0):
    print ("\n¡Debes ingresar un valor mayor a 0!")
    y = int(input("\nIngrese otro numero entero:\n\n→ "))

def función (x,y):
    if x > y: return 1
    elif x < y: return -1    
    elif x == y: return 0
print (función(x,y))