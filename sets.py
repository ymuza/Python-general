# los sets parecen diccionarios, pero no tienen keys, y estan separados por comas.
# LOS SETS NO ACEPTAN VALORES DUPLICADOS,
# por lo que eliminan automaticamente aquellos DUPLICADOS.

objeto_cualquiera = "custom object"
my_data_type = {1, 2, False, 4, "yamil", objeto_cualquiera, 5.0, 1}
print(my_data_type)  # los sets no tienen orden, entonces cada vez que imprimamos , van a aparecer valores ordenados de forma aleatoria.
print(type(my_data_type))
