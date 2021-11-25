# imprimir números del 1 al 10 usando recursividad

def f1(x):
    x = x + 1
    print(x)
    if x != 10:
        f1(x)


f1(1)
