my_dict = {'name': 'pedro', 'lastname': 'gomez'}

print(my_dict)

print("\n")

my_dict2 = {'age': '26', 'height': '1.85 mts'}

my_list = [dict(my_dict)]

print(my_list)
print("\n")
my_list.append(dict(my_dict2))
print(my_list)

print("\n")

t = my_dict2['height']
print(t)

print("\n")
my_dict3 = {'weight': '80 kgs', 'shoe size': '13 us'}

my_dict2['weight'] = my_dict3['weight']

print(my_dict2)
