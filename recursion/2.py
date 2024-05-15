"""
Implement a recursive method to order a list
"""
def order(list1, quantity):
    if quantity > 1:
        for f in range(0, quantity - 1):
            aux = list1[f]
            list1[f] = list1[f + 1]
            list1[f + 1] = aux
        order(list1, quantity - 1)


data = [60, 44, 22, 33, 2]
print(data)
order(data, len(data))
print(data)
