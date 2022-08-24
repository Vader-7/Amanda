print("INGRESE CORREO.")
correo = input("\n-->\t")
while correo.count("@") == 0 or correo.count(".") == 0:
    print("CORREO INVALIDO.")
    correo = input("\n-->\t")
print("INGRESE CONTRASEÑA.")

