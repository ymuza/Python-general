#los generadores son rutinas o subprogramas usados para controlar el comportamiento de un iterador en un bucle.


def topten():
    n = 1
    while n <= 10:
        square = n*n
        n = n+1
        yield square


print(type(topten()))
for i in topten():
    print(i)


