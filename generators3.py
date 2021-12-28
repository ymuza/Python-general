def multiples(numbers):
    for item in range(len(numbers)):  # con 'range' busco en el rango que 'len' retorna
        yield numbers[item] * 2


number_list = [1, 2, 3, 4, 5]

for i in multiples(number_list):
    print(i, end='')
    print('')
