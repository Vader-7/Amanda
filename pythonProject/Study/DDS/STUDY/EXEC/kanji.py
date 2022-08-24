def get_sum(a, b):
    x = 0
    if a < b:
        for i in range(a, b + 1):
            x += i
        return x
    elif a > b:
        for i in range(b, a + 1):
            x += i
        return x
    else:
        return a


print(get_sum(-10, 20))

"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns 
the result. 

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a, b):
    lista = []
    for z in b:
        for x in a:
            if x == z:
                lista.append(z)
    a = [x for x in a if x not in lista]
    return a


uno = [1, 2, 2]
dos = [2]
print(array_diff(uno, dos))

"""a.reverse()
b.append(a[0])
a.pop(0)
return a"""
