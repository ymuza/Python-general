import copy

dict1 = {23, 4, 5, 6}
dict2 = dict1

print(id(dict1))
print(id(dict2))

old_list = [[1, 2, 4], [5, 6, 7], [8, 9, 10]]

new_list = copy.copy(old_list)
new_list[0][2] = 'c'

print("old list: ", old_list)
print("new list: ", new_list)

