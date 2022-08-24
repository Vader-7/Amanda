# EJERCICIOS INFORMATICA BIOMEDICA 2
while True:
    try:
        num1 = int(input("\n-->\t"))
        num2 = int(input("\n-->\t"))
        division = num1 / num2
        break
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR POR 0.\nREINGRESE")
    except ValueError:
        print("VALOR INGRESADO INVALIDO.\nREINGRESE")
print(f"LA DIVISIÓN ES:\t{round(division)}")
