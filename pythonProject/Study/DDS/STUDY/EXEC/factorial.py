# Factorial
x = int(input("Ingrese un numero:\n\t-->\t"))
y = 1
fact = 1
while y <= x:
    fact = fact * y
    y = y + 1
print(f"El factorial del numero {x} es: {fact}")
