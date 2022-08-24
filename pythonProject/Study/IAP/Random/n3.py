import random

largo_arreglo=0
arreglo=[]

while largo_arreglo<10:
    num=random.randint(0,100000)
    arreglo.append(num)
    largo_arreglo+=1
#print(arreglo)
num_ingresado=int(input("ingrese un número: "))
if num_ingresado in arreglo:
    print(f"el numero {num_ingresado} se encuentra en la lista",format(num_ingresado))
else:
    print(f"el numero {num_ingresado} no se encuentra en la lista",format(num_ingresado))