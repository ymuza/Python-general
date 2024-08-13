def separate():
    """moves odd numbers to the front of the list"""

    list1 = [1, -2, 3, -4, 5, -6]
    pos = 0
    for i, number in enumerate(list1):
        if number < 0:
            temp = number
            list1[i] = list1[pos]
            list1[pos] = temp
            pos += 1

    print(list1)


#separate()


def sort_largest_sequence():
    list1 = [11, 0, 65, 80, 90, 43, 15, 23]
    pos = 0
    bigest = 0

    numbers = {x: 0 for x in list1}
    print(numbers)

    for i, num in enumerate(list1):
        if num > list1[i]:
            temp = list1[pos + 1]
            list1[pos + 1] = temp

        pos += 1


sort_largest_sequence()


#sum the four largest elements
def order_and_sum():
    list1 = [11, 0, 65, 80, 90, 43, 15, 23]

    pos = 0

    for i, number in enumerate(list1):
        temp = list1[i]
        list1[i] = list1[pos]

        pos += 1


order_and_sum()
