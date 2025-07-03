

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



def switch_elements(number1, number2, lst):
    """Switch two Elements"""
    try:
        pos1 = lst.index(number1)
        pos2 = lst.index(number2)
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst
    except ValueError:
        print(f"One or both elements not found in list")
        return lst




l = [10, 5 ,4 , 1, 8, 9, 22, 11, 19]
print((switch_elements(9, 19, l)))