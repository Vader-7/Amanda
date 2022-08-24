def validaRut(p_rut):
    while p_rut < 4000000 or p_rut > 20000000:
        print("Rut ingresado invalido.")
        p_rut = int(input("-->"))
    return p_rut


while True:
    print("Ingrese su rut")
    rut = validaRut(int(input("-->")))
    break
