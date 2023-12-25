
# excluir de un listado de numeros aquellos divisibles por 3
for i in range(1, 21):
    if i % 3 == 0:
        continue  # con este continue estamos diciendo que ignore aquellos divisibles por 3
    print(i)


# imprimir los numeros de un listado excluyendo los impares
for i in range(1, 21):
    if i % 2 != 0:
        pass  # si se cumple la condicion de arriba, no se ejecuta nada y continua al else
    else:
        print(i)
