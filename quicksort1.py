
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  # removes the last element and return it

    items_greater = []  # list to store the greater than the pivot items

    items_lower = []  # list to store the lower than the pivot items

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    items_sum = items_lower + items_greater

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
    # la linea de arriba va a llamar al algoritmo, poniendo de izquierda a derecha los menores al pivot y
    # de derecha a izquierda a los mayores al pivot


print(quick_sort([4456, 6, 213, 43, 67, 3]))
