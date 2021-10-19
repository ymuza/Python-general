
users = [
         (0, "bob", "password"),
         (1, "Rolf", "fvvvv12"),
         (2, "Jose", "long32323"),
         (3, "Paco", "ddvdv1111aaa"),
        ]

username_mapping = {user[0]: user for user in users}  # user[1] es la key. El 1 corresponde al nombre (va a mostrar el nombre primero), y user antes del for es el value

print(username_mapping)


# ----------------------------

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

identifier, username, password = username_mapping[username_input]
""" en la linea de arriba, se va a comparar el pass y el user ingresado con 
la informacion de la tupla (los users y pass) mapeada en username_mapping."""

if password_input == password:  # password recibe de username_mapping, el password para el username_input
    print("your details are correct.")  # compara el pass ingresado con el que está en la tupla, para el user ingresado
else:                                   # y va a devolver correcto si es el mismo pass logicamente.
    print("your details are not correct.")



