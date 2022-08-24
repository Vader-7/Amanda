# PRUEBA 1 CON FUNCIONES
def calcImc(p_peso, p_altura):
    p_imc = (p_peso / (p_altura * p_altura))
    return p_imc


def informe(p_imc):
    if 18.5 <= p_imc <= 24.9:
        return "NORMAL"
    elif 25 <= imc <= 29.9:
        return "SOBREPESO"
    elif 30 <= imc <= 34.9:
        return "GRADO1"
    elif 35 <= imc <= 39.9:
        return "GRADO1"
    elif imc >= 40:
        return "GRADO1"


def menu():
    print("""
        1.- CALCULAR IMC.
        2.- INFORME.
        3.- SALIR.
        """)


# VARIABLES
opcion = 0
normal = 0
sobre = 0
grado1 = 0
grado2 = 0
grado3 = 0
pacientes = 0
imc = 0

while opcion != 3:
    menu()
    try:
        opcion = int(input("\n-->\t"))
    except ValueError:
        print("OPCION INGRESADA INVALIDA.")
    if opcion == 1:
        while True:
            try:
                print("INGRESE PESO.")
                peso = float(input("\n-->\t"))
                print("INGRESE ALTURA.")
                altura = float(input("\n-->\t"))
                break
            except ValueError:
                print("OPCION INGRESADA INVALIDA")
        imc = round(calcImc(peso, altura))
        print(f"EL IMC DEL PACIENTE ES:\t{imc}")
        if "NORMAL" in informe(imc):
            print("CLASIFICACION: NORMAL.")
            normal += 1
        elif "SOBREPESO" in informe(imc):
            print("CLASIFICACION: SOBREPESO.")
            sobre += 1
        elif "GRADO1" in informe(imc):
            print("CLASIFICACION: OBESIDAD GRADO 1.")
            grado1 += 1
        elif "GRADO2" in informe(imc):
            print("CLASIFICACION: OBESIDAD GRADO 2.")
            grado2 += 1
        elif "GRADO3" in informe(imc):
            print("CLASIFICACION: OBESIDAD GRADO 3.")
            grado3 += 1
        # CONTADOR DE PACIENTES
        pacientes += 1
        # REINICIO
        altura = 0
        peso = 0
    elif opcion == 2:
        print(f"""
        PACIENTES:\t{pacientes}
        PACIENTES NORMALES:\t{normal}
        PACIENTES CON SOBREPESO:\t{sobre}
        PACIENTES CON OBESIDAD GRADO 1:\t{grado1}
        PACIENTES CON OBESIDAD GRADO 2:\t{grado2}
        PACIENTES CON OBESIDAD GRADO 3:\t{grado3}""")
    elif opcion == 3:
        print("ADIOS.")
    else:
        print("OPCION INGRESADA INVALIDA.")
