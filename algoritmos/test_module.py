

# def move_specific_element_to_the_end(number, lst):
#     """Move Specific Element to the End. If element is 3, Output should be: [1, 2, 4, 3, 3, 3]"""
#
#     temp = []
#
#     for index, value in enumerate(lst[:]):
#         if value == number:
#             lst.remove(value)
#
#     lst.append(number)
#     print(lst)
#
#
#
#
# l = [10, 5 ,4 , 4, 1, 8, 9, 22, 11, 19]
# (move_specific_element_to_the_end(4, l))



def zeroes_to_the_end():
    """move 0 to the end of the list"""
    list1 = [10, 0, 20, 0, 40, 60]
    pos = 0
    for v in list1:
        if v != 0:
            list1[pos] = v
            pos += 1

    while pos < len(list1):
        list1[pos] = 0
        pos += 1
    return list1















print(zeroes_to_the_end())