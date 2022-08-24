"""#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)"""

i = 2
while i >= 0:
    print("*")
    i -= 2

for i in range(-1, 1):
    print("#")

z = 10
y = 0
x = z > y or z == y
print(x)

lst = [3, 1, -1]
lst[-1] = lst[-2]
print(lst)

vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
print(vals)

nums = []
vals = nums
vals.append(1)
print(vals)
print(nums)

nums = []
vals = nums[:]
vals.append(1)
print(vals)
print(nums)

lst = [0 for i in range(1, 3)]
print(lst)

lst = [0, 1, 2, 3]
x = 1
for elem in lst:
    x *= elem
print(x)

nums = [1, 1]
vals = nums
print(vals)
print(nums)

"""def func1 (a):
    return None

def func2 (a):
    return func1(a) * func1(a)

print(func2(2))"""

print(1 // 2)


# def func(a, b):
# return b ** a

# print(func(b=2, 2))


def fun(t, k):
    if t == k:
        return k
    else:
        return fun(t, k - 1)


print(fun(0, 3))


def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

lst = [1, 2]

for v in range(2):
    lst.insert(-1, lst[v])

print(lst)
