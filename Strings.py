import string

my_message = "hello \"hoe-ass\" bitches"

other_message = " ,regulate"

print(my_message)

my_message2 = my_message + "" + other_message


print(my_message2)

print("----------------------")
print("")

#  ---------Slicing--------------------------------------

name = "interstellar"

print(name[-1])  # imprime el ultimo caracter del string (lo uso si no sé la cantidad de caracteres que tiene)

print(name[0:5])  # imprime los caracteres del 0 al 5 ("inter")

print(name[5:])  # imprime los caracteres a partir del quinto hasta el último

print(name[:5])  # imprime desde el primer caracter hasta el quinto

print(name[:])  # imprime todos los caracteres

print(name[0:6:2])  # imprime del 0 al 6 pero salteandose 1(el step size, que en este caso es 2)

print(name[::2])  # imprime todos los caracteres salteandose 1

print(name[::-1])  # imprime todos los caracteres al revés (del último al primero)

print("-----------------------")
print("")

  # Métodos y funciones que se pueden usar sobre strings (len(), type(), id(), capitalize(), upper(), lower(), find(), strip(), split(), join(), import string )--------

greeting = "hello"
user = "Yamil"
message = "Welcome to the algorithms course"
my_languages = ['Python', 'Ruby', 'Javascript']

print(greeting, user, message)  # imprime los 3 strings uno al lado del otro

print(len(greeting))  # imprime la cantidad de caracteres del string 'greeting' INCLUYENDO los espacios en blanco (ejemplo de esto abajo)
print(len(message))
print("\n")
print(type(message))  # dice que de tipo es la variable 'message'
print("\n")
print(user.capitalize())  # primera letra mayuscula
print("\n")
print(user.upper())  # todo en mayuscula
print("\n")
print(user.lower())  # todo en minuscula
print("\n")
print(greeting, user, message.strip().lower())  # strip() saca los espacios en blanco por default . Acá se concatenan funciones
print("\n")
print(message.find('course'))  # Busca la palabra entre parentesis en ese string. Si no la encuentra, devuelve -1
print("\n")
print(message.split())  # Separa strings según los espacios en blanco. Entre parentesis, se especifica porque lo quiero separar (en este caso, espacios en blanco)
print("\n")
print("-".join(my_languages))  # junta strings mediante '-'
print("\n")

  # ------print formating & special caracteres--------------------

stock_price = "1100"
todays_price = "1100"
yesterday_price = "1000"

print("Today's price for google stock is: {}".format(stock_price)) # format mete el stock_price dentro de los corchetes.
print("\n")
print(f"Today's price for google stock is: {stock_price}")  # interpolación (hay una 'f' antes del string de caracteres)
print("\n")
print(f"Today's price:{todays_price}, yesterday's price:{yesterday_price}")  # otro ejemplo de interpolación de strings
print("\n")
print("\n")

 # --------------math, type, input--------------------------------

type(4)
