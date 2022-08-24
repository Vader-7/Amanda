# EJERCICIOS Ty
import time

# 1.
cuatro = 0
cadena = input("\n-->\t")
for char in cadena:
    if char == "4":
        cuatro += 1
print(f"EL NUMERO 4 SE ENCUENTRA {cuatro} VECES EN LA CADENA.")
# 2.
x = int(input("\n-->\t"))
y = int(input("\n-->\t"))
suma = y + x
if 15 <= suma <= 20:
    print("LA SUMA ES:\t20")
else:
    print(f"LA SUMA ES:\t{suma}")
# 3.
a = int(input("\n-->\t"))
b = int(input("\n-->\t"))
c = int(input("\n-->\t"))
suma = a + b + c
if a == b or b == c or a == c:
    print("LA SUMA ES\t0")
else:
    print(f"LA SUMA ES:\t{suma}")


# 4.


def mostrar(p_nombre, p_edad, p_direccion):
    print(f"""
            NOMBRE:\t\t{p_nombre}
            EDAD:\t\t{p_edad}
            DIRECCIÓN:\t{p_direccion}
        """)


print("INGRESE NOMBRE.")
nombre = input("\n-->\t")
while nombre is None or nombre == "" or len(nombre) < 3 or not nombre.isalpha():
    print("NOMBRE INGRESADO INVALIDO.")
    nombre = input("\n-->\t")
while True:
    try:
        print("INGRESE EDAD.")
        edad = int(input("\n-->\t"))
        if 0 < edad < 110:
            print("EDAD INGRESADA.")
            break
        else:
            print("EDAD INVALIDA.")
    except ValueError:
        print("VALOR INGRESADO INVALIDO")
while True:
    print("INGRESE DIRECCION.")
    direccion = input("\n-->\t")
    if len(direccion) > 3:
        print("DIRECCION INGRESADA.")
        break
    else:
        print("DIRECCION INVALIDA.")

mostrar(nombre, edad, direccion)

# 5.
print("INGRESE NOMBRE.")
nombre = input("\n-->\t")
while nombre is None or nombre == "":
    print("CAMPO VACIO, REINGRESE.")
    nombre = input("\n-->\t")
# 6.
nom1, nom2, nom3 = [str(i) for i in input("-->").split()]
print(f"""
    NOMBRE 1.\t{nom1}
    NOMBRE 2.\t{nom2}
    NOMBRE 3.\t{nom3}
    """)
# 7.
nombreCompleto = None
nombre = input("INGRESE NOMBRE.\n-->\t")
while len(nombre) < 3:
    nombre = input("NOMBRE INVALIDO.\n-->\t")

apellido = input("INGRESE APELLIDO.\n-->\t")
while len(apellido) < 3:
    apellido = input("APELLIDO INVALIDO.\n-->\t")

nombreCompleto = nombre + " " + apellido
print(f"Hola\t{nombreCompleto}.")

# DESAFIO


user = "Tyler"
pasw = "123"
opcion = 0
promedio = 0


def menu():
    print("""
            1.- CALCULAR PROMEDIO.
            2.- SALIR.
        """)


while opcion != 2:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
    if opcion == 1:
        print("INGRESE USUARIO:")
        usuario = input("\n-->\t")
        print("INGRESE CONTRASEÑA:")
        contra = input("\n-->\t")
        if user != usuario or contra != pasw:
            print("CONTRASEÑA O USUARIO INVALIDO.")
        else:
            print("INGRESE NOMBRE DEL ALUMNO.")
            alumno = input("\n-->\t")
            while alumno is None or alumno == "":
                print("CAMPO VACIO.")
                alumno = input("\n-->\t")
            print("INGRESE LA CANTIDAD DE NOTAS QUE VA INGRESAR.")
            cant = int(input("\n-->\t"))
            while 5 < cant < 3:
                print("CANTIDAD DE NOTAS INVALIDO.")
                cant = int(input("\n-->\t"))
            for i in range(cant):
                print(f"INGRESE LA {i + 1} NOTA.")
                nota = int(input("\n-->\t"))
                suma += nota
            promedio = round(suma / cant)
            print(f"EL PROMEDIO DEL ALUMNO {alumno.upper()} ES:\t{float(promedio)}")
            time.sleep(3)
    elif opcion == 2:
        print("ADIOS.")
        break
    else:
        print("OPCION INGRESADA INVALIDA.")
