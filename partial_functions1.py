from functools import partial


# return true if > 20 without using partial functions
# ---------------------------------------------------
def greater_than(a, b):
    return a > b


def make_comparator(n):
    return lambda a: a > n


greater_than_20 = make_comparator(20)

print(greater_than_20(10))
print(greater_than_20(20))
print(greater_than_20(30))


# return true if > 20 using a partial function
# ---------------------------------------------
def greater_than_using_partial(a, b):
    return a > b


greater_than_20 = partial(greater_than_using_partial, 20)

print(greater_than_20(10))
print(greater_than_20(20))
print(greater_than_20(30))

