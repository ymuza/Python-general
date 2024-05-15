"""Given dictionary is consisted of vehicles and their weights in kilograms.
Contruct a list of the names of vehicles with weight below 5000 kilograms.
In the same list comprehension make the key names all upper case."""

dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

lst = [i.upper() for i in dict1 if dict1[i] < 5000]

print(lst)


"""Construct a list from the squares of each element in the list, if the square is greater than 50."""

lst1 = [2, 4, 6, 8, 10, 12, 14]

lst2 = [i**2 for i in lst1 if i**2 > 50]

print(lst2)


""""""


