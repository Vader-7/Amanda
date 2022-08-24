# VALIDA CONTRASEÑA
print("INGRESE SU CONTRASEÑA.")
contra = input("\n-->\t")
while len(contra) < 8 or contra.islower() or contra.isupper():
    print("CONTRASEÑA INVALIDA.")
    contra = input("\n-->\t")