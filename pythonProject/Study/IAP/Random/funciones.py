def calcularIMC(masa, estatura):
    imc = masa / (estatura * estatura)
    return imc


def calcularIVA(base):
    iva = base - (base * 0.19)
    return iva


def calcularDES():
    valor = int(input("Ingrese el valor del producto: "))
    des = int(input("Ingrese el descuento del producto: %"))
    descuento = valor - (valor * (des / 100))
    return descuento
