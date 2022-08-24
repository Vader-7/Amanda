import random

# name = "Tyler"
# age = 22
# print(f"\nName:\t{name}\nAge:\t{age}")

# LISTAS

cantidadE = int(input("Ingrese la cantidad de empleados que va ingresar a sistema.\n\t-->\t"))
numbers = [23, 13, 56, 565, 23]
friends = ["Tomas", 27, False]
print("\n\n")
print(friends)
print("\n\n")
friends[0] = "Matías"
print(friends)
print("\n\n")
friends.extend(numbers)
print(friends)
print("\n\n")
for i in range(cantidadE):
    nombreN = input("Ingrese el nombre: ")
    friends.append(nombreN)
print("\n\n")
print(friends)
print("\n")
print(type(friends))

print("\n")
# Float numbers
x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(type(x))
print(type(y))
print(type(z))

print("\n")
# Complex numbers
x = 3 + 5j
y = 5j
z = -5j

print(y + x)
print(type(x))
print(type(y))
print(type(z))

print("\n")
# Casting
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random use
print(random.randrange(1, 2913192312))

# Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


# IFS
a = 33
b = 200
# Pass for simple IF
if b > a:
    pass
# IF inside
x = 41

if x > 10:
    print("Above ten,")
    if x <= 20:
        pass
    else:
        print("and also above 20!")
else:
    print("but not above 20.")

