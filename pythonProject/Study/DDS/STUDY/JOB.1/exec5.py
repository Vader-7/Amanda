# EJERCICIOS INFORMATICA BIOMEDICA 5
def calculaPromedio(cant):
    suma = 0
    for i in range(cant):
        print(f"INGRESE LA {i + 1} NOTA:")
        nota = float(input("\n-->\t"))
        suma += nota
    prom = round(suma / cant, 1)
    return prom


while True:
    try:
        print("INGRESE LA CANTIDAD DE NOTAS.")
        cant1 = int(input("\n-->\t"))
        break
    except ValueError:
        print("DATO INGRESADO INVALIDO.")
promedio = calculaPromedio(cant1)
if promedio < 4:
    print(f"EL ALUMNO REPROBO LA ASIGNATURA CON NOTA {promedio}")
else:
    print(f"EL ALUMNO APROBO LA ASIGNATURA CON NOTA {promedio}")
