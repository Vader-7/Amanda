dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
signo = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio",
         "Sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

mes = mes - 1
if dia > fechas[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print(f"Día: {dia}\nMes {mes}\n\n")
print("Signo:" + signo[mes])
print("\nDescripción: Alitas de pollo tienes que comer si felicidad es lo que deseas tener.")
