opción = 0
horóscopo = 0
while opción != 3:
    print("\n\t\tHORÓSCOPO")
    print("\t(1)\tConsultar su Signo.")
    print("\t(2)\tConsulta Horóscopo.")
    print("\t(3)\tSALIR.")
    try:
        opción = int(input("\t->\t"))
    except:
        print("\t\tOpción Ingresada Invalida, ingrese un numero.")

    if opción == 1:
        dia = int(input("Ingresa el día de su nacimiento: "))
        mes = int(input("Ingresa el mes de su nacimiento: "))
        horóscopo = horóscopo + 1
        if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Aries")
        if (dia >= 21 and mes == 4) or (dia <= 21 and mes == 5):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Tauro")
        if (dia >= 22 and mes == 5) or (dia <= 21 and mes == 6):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Géminis")
        if (dia >= 21 and mes == 6) or (dia <= 23 and mes == 7):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Cáncer")
        if (dia >= 24 and mes == 7) or (dia <= 23 and mes == 8):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Leo")
        if (dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Virgo")
        if (dia >= 24 and mes == 9) or (dia <= 23 and mes == 10):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Libra")
        if (dia >= 24 and mes == 10) or (dia <= 22 and mes == 11):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Escorpio")
        if (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Sagitario")
        if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Capricornio")
        if (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Acuario")
        if (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
            print(f"\n\nDía: {dia}\nMes: {mes}\n\nSigno: Piscis")
    if opción == 2:
        if horóscopo == 0:
            print("\tNo tenemos datos registrados.")
        else:
            if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Deberías comer mas.")
            if (dia >= 21 and mes == 4) or (dia <= 21 and mes == 5):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Toma mas agua.")
            if (dia >= 22 and mes == 5) or (dia <= 21 and mes == 6):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Encontraras el amor en un KFC.")
            if (dia >= 21 and mes == 6) or (dia <= 23 and mes == 7):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: El cáncer es malo.")
            if (dia >= 24 and mes == 7) or (dia <= 23 and mes == 8):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Recuerda, Leo Rey es BRÍGIDO.")
            if (dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
                print(
                    f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Ser el mejor Signo Zodiacal significa una mayor responsabilidad.")
            if (dia >= 24 and mes == 9) or (dia <= 23 and mes == 10):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: 彼らがジェミニに言うことはおそらく嘘です.")
            if (dia >= 24 and mes == 10) or (dia <= 22 and mes == 11):
                print(
                    f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Si felicidad tu deseas, Alitas de pollo tu debes comer.")
            if (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: More pls eat.")
            if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: Recuerda siempre debes programar cuando....")
            if (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: 1 + 1 = 10.")
            if (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
                print(f"\n\nDía: {dia}\nMes: {mes}\n\tDescripción: もっと食べてください.")
