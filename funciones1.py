
print("type the first number: ")
num1 = float(input())

print("type the second number: ")
num2 = float(input())


def sums(num1, num2):
    return num1 + num2


def subs(num1, num2):
    return num1 - num2


def multip(num1, num2):
    return num1 * num2


def divi(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:
        print("There's an error:", e)


def average(sums):
    return sums / 2


print("chose an option: 1-adding, 2-subtraction, 3-multiplication, 4-division, 5-average. Any other number exits.")
op = int(input())
if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:

    if op == 1:
        chosen_op = (sums(num1, num2))
        print(f"The result of the sum is: {chosen_op}")

    elif op == 2:
        chosen_op = (subs(num1, num2))
        print(f"The result of the subtraction is: {chosen_op}")

    elif op == 3:
        chosen_op = (multip(num1, num2))
        print(f"The result of the multiplication is {chosen_op}")

    elif op == 4:
        chosen_op = (divi(num1, num2))
        if chosen_op is not None:
            print(f"The result of the division is {chosen_op}")

    elif op == 5:
        chosen_op = (average(sums(num1, num2)))
        print(f"Both numbers average is: {chosen_op}")
else:
    print("The program ended.")
