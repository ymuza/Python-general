def person(name, **kwargs):

    print(name)
    for i, j in kwargs.items():
        print(i, j)


person('navin', age=28, city='mumbai', mob=33333)
