list = [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(list))


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums)
print(vals)

y = int(input())
x = int(input())
x = x % y
x = x % y
y = y % x
print(f"\t\n", y)

x = 1 // 5 + 1 / 5
print(x)

x = float(input())
y = float(input())
print(y ** (1 / x))

lst = [i for i in range(-1, -2)]
print(lst)
