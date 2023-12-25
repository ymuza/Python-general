
def staircase(steps):
    for i in range(1, steps + 1):
        print(" " * (steps - i), ("#" * i))


n = int(input("insert the number of steps of in the staircase: "))
staircase(n)

