my_lambda = lambda z: z ** 3  # creo una variable lambda que va a ser igual a la funcion anonima de x
print(my_lambda(5))
print(my_lambda(7))

print("\n")

my_letters = ['a', 'b', 'c']

print(list(map(lambda r: r + r.capitalize(), my_letters)))  # uso map para

x = [1, 2, 4, 5]
bigger_than_2 = filter(lambda p: p >= 2, x)

print(list(bigger_than_2))  # si imprimo solo 'bigger_than_2' lo imprime como filter object, por eso el list
