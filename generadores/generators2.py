my_list = [x for x in range(1, 10)]


# sin generador. Retorna la lista entera. Se itera por todos los items de la lista.
def process_list(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2  # multiplica cada item de la lista por 2
    return my_list


# con generador. En este caso estamos retornando cada item de forma individual, entonces se ahorra memoria
def process_list_with_generator(my_list):
    for i in range(len(my_list)):
        yield my_list[i] * 2


for item in my_list:
    print(item, end='')
    print('')

for item in process_list(my_list):
    print(item, end=' ')
    print('')

for item in process_list_with_generator(my_list):
    print(item, end='')
print('')
