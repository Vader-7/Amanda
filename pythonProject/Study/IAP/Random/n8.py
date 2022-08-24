palíndromo = input("Ingrese su palabra:\n")

if str(palíndromo)==str(palíndromo)[::-1]:
	print(f"La palabra ({palíndromo}) es un palíndromo")
else:
	print(f"({palíndromo}) no es un palíndromo")

def contar_letras():
	c = 0
	for i in palíndromo:
		if(i.isalpha()):
			c = c + 1
	print(f"Numero de letras: {c}")
contar_letras()