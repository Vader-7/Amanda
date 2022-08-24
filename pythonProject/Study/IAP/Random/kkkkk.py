"""for k in "Hola":
    print (k, end = ' ')"""

"""t = int(input("Ingrese Tope: "))
a = 0
b = 1
c = 0
for x in range(t):
    c = a + b
    b = a
    a = c
    print(b)
    if c > t:
        break"""

"""f = 1
x = int(input("\n\t\tIngrese su numero: "))
print("\n\t\t")
for i in range(x):
    f *= (x - i)
    print(f, end=' ')"""

lista_agenda=[]
contador=0
respuesta=1

while(respuesta==1):#TRUEKT

  lista_agenda.append(input("Ingrese su nombre:\n"))
respuesta=int(input("Desea mas registros?:Presione \n1 para SI\n2 para NO\n"))
contador=contador+1

for x in range(contador):
    print(lista_agenda[x])
