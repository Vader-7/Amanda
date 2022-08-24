# EJERCICIOS INFORMATICA BIOMEDICA 3
print("INGRESE SU CONTRASEÑA")
contra = input("\n-->\t")
while len(contra) < 8 and contra != contra.islower() and contra != contra.isupper():
    print("CONTRASEÑA INVALIDA REINGRESE.")
    contra = input("\n-->\t")
print("CONTRASEÑA INGRESADA.")
