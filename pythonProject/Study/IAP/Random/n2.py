ls1 = ["Hola", "K", "Mar", "Efe", "Casa", "Zeta", "Ram", "K"]
ls2 = ["Ola", "Ram", "Edificio", "Home", "Vaca", "K"]
c = 0


# se puede agregar un contador para contar datos y no se repitan
def repetidos(ls1, ls2):
    ls3 = []
    for i in ls1:
        for j in ls2:
            if i == j:
                ls3.append(i)
    print(ls3)


repetidos(ls1, ls2)


def duplicado(lista):
    return list(set([i for i in lista if lista.count(i) > 1]))


print("Valor duplicado mas de una vez en la lista 1: ", duplicado(ls1))
print("Valor duplicado mas de una vez en la lista 2: ", duplicado(ls2))
