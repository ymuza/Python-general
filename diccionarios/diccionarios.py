 # los diccionarios tienen pares de elementos, donde uno de los elementos de esos pares es la key.

objeto_cualquiera = "custom object"
my_data_type = {1: "hello", 2: "yamil", 3: None, 4: objeto_cualquiera, 5: 5.0}

# print(my_data_type["hello"]) #imprime el dato que se encuentra anexado a la key correspondiente (en este caso, "hello")

my_dict = {'name': 'john', 'course': 'python'}

my_dict2 = {'name': 'lucas', 'course': 'ruby'}

my_dict3 = {'board_name': my_dict2["name"]}

print(my_dict3)
dictTest = my_data_type[1]

print(dictTest)

names = my_dict["name"]

print('\b')

