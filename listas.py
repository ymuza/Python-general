
#  Las listas son conjuntos de distintos tipos de datos.

objeto_cualquiera = "custom object"
my_data_type = [1, 2, False, 4, "yamil", objeto_cualquiera, 5.0, 1]

print(my_data_type[3])  # imprime el dato que se encuentra en la posición 3 de la lista (empieza en la posición 0).
print(type(my_data_type))

print("\n")

my_data_type2 = [43, 567, 3, 523, 1, 2, 9, 0]

my_data_type2_sorted = sorted(my_data_type2)
my_data_type2.sort()  # el metodo sort organiza la lista como con 'sorted'
print(f"sorted list-> {my_data_type2_sorted}")
print("\n")
print(f"sorted list but with the method sort()-> {my_data_type2}")


p = 36
my_data_type2.append(p)

print("\n")

print(f'new my_data_type is {my_data_type2}')
