"""
create a list with random numbers, then create an empty list
and fill said list with the square root of the elements of the
first list.
"""
list1 = [6, 7, 8, 23, 45, 67]

list2 = []

for element in list1:
    list2.append(element * element)
print("list1 is " + str(list1))
print("list2 is " + str(list2))

print("\n")
"""
having a list with tuples filled with people names and ages,
generate a new list with the people under 21 years old. 
"""
people = [('luke', 33), ('lucy', 19), ('richard', 15), ('anabelle', 39), ('martha', 43)]

under_age_people = [uap for uap in people if uap[1] <= 21]  # en uap[1], 1 es el value

print(under_age_people)

print("\n")

"""
Generate a list with all multiple values of 8 between 1 and 500. 
"""
multiples_of8 = [value for value in range(1, 501) if value % 8 == 0]
print(multiples_of8)
