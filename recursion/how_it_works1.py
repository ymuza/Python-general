def first_method():
    second_method()
    print("first method")

def second_method():
    third_method()
    print("second method")

def third_method():
    fourth_method()
    print("third method")

def fourth_method():
    print("fourth method")



first_method()