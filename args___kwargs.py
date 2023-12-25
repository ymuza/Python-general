def person(name, **kwargs):  # variable length arguments
    print(kwargs)
    print(name)
    for i, j in kwargs.items():
        print(i, j)


person('navin', age=28, city='mumbai', mob=33333)


