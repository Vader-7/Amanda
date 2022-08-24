import re


def validaNombre(p_nombre_apellido):
    if re.match(r"^[a-zA-Z].+[a-zA-Z]$", p_nombre_apellido):
        return False
    else:
        return True


while validaNombre(input("INGRESE NOMBRE Y APELLIDO: ")):
    pass
