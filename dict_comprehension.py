import pdb

print("Enter a number: ")
num1 = float(input())
print("Enter a second number: ")
num2 = float(input())


def sums(a, b):
    return a+b


def substract(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


op = int(input("select an operation (1-sum, 2-subst, 3-divide, 4-multip): "))

my_dict2 = {1: sums, 2: substract, 3: divide, 4: multiply}

selected_op = my_dict2[op](num1, num2)

print("the result is: " + str(selected_op))

