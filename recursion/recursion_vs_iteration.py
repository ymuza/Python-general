
"""recursive function vs iterative function"""

"""recursive function"""
def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n-1)
        return power * 2


"""iterative function"""
def power_of_two_iterative(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
        return power
