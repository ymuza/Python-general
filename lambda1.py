
my_lambda = lambda x: x**3  #creo una variable lambda que va a ser igual a la funcion anonima de x
print(my_lambda(5))
print(my_lambda(7))

print("\n")

my_letters = ['a', 'b', 'c']

print(list(map(lambda x: x+x.capitalize(), my_letters)))  # uso map para
