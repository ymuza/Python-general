"""Prints a right-aligned staircase of '#' characters."""

def staircase(steps):
    """Prints a staircase of `steps` rows, right-aligned with '#'."""
    for i in range(1, steps + 1):
        print(" " * (steps - i), ("#" * i))


if __name__ == "__main__":
    try:
        n = int(input("insert the number of steps of in the staircase: "))
    except ValueError:
        print("please enter a valid number.")
    else:
        staircase(n)
