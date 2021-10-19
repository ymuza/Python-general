def sum():
    a = 4
    def sum2():
        nonlocal a
        print(a+2)

    sum2()

