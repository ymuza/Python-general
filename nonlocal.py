def suma():
    a = 4

    def suma2():
        nonlocal a
        print(a + 2)

    suma2()
