# con un for
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = []

for a in list1:
    if a % 2 != 0:
        print(a)

# usando list comprehension:
print("\n")

list2 = [10, 21, 4, 45, 66, 93]

just_odd = [num for num in list2 if num % 2 == 1]

print(f"the odds are {just_odd}")
