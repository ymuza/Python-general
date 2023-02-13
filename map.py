"""map returns an iterator that applies a function to every item of iterable"""
"""map(function, iterable)"""

# convert from celcius to fahrentheit & viceversa

# to convert o to Fahrentheit => F = (9/5)*C+32

temps_in_C = [('berlin', 29), ('Cairo', 36), ('Buenos Aires', 19)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

temps_in_F = list(map(c_to_f, temps_in_C))

print(temps_in_F)



# make even numbers by adding a 1 to odd numbers

def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num

x = [551, 145, 323, 457, 789]

y = list(map(make_even, x)) #  lo transformo en lista sino devuelve el tipo de objeto solamente




print(y)
