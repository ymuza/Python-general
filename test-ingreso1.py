def f1():
    x = -1
    print("Baby")


def f2(method, x):
    if x < 0:
        return method()
    else:
        x = x - 1
        print("Ice")
        f2(method, x)


def main():
    f2(f1, 2)


x = 3
main()
