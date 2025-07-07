# ESTE MÓDULO ES PARA PRACTICAR, NADA MÁS
from nltk.sem.chat80 import country

#
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


# def move_all_instances_of_element_to_the_end(number, list1):
#
#     clean_list = [n for n in list1 if n != number]
#     number_occurrences = list1.count(number)
#
#     return clean_list + [number] * number_occurrences
#
#
#
# print(move_all_instances_of_element_to_the_end(3, [3, 5, 6, 45, 3, 88, 99, 10, 4, 3]))


def anagram_checker(w1, w2):

    w1 = sorted(w1.replace(" ", "").lower())
    w2 = sorted(w2.replace(" ", "").lower())

    return w1 == w2

print(anagram_checker("casa", "a   cas"))


