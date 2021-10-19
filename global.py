x = 5
def func1():
    global x #tengo que avisar al codigo que x no es una variable nueva sino la variable global x = 5
    x += 3
    print(x)

def func2():
    print(x)


func1()
func2()