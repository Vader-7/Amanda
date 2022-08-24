import numpy

bus = numpy.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32],
    [33, 34, 35, 36],
    [37, 38, 39, 40]
])
for i in range(10):
    for j in range(4):
        if j == 2:
            print("\t", bus[i][j], end=" ")
        else:
            print(bus[i][j], end=" ")
    print("\n")
