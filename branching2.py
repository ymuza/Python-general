  # ----------------elif--------------------------

  # elif permite hacer varias variantes del if, mientras que un else permite solo otro caso.

op = int(input("select an operation (1-sum, 2-subst, 3-multip, 4-div): "))

if op == 1 or op == 2 or op == 3 or op == 4:

    print("Enter a number: ")
    num1 = float(input())
    print("Enter a second number: ")
    num2 = float(input())

    if op == 1:
        result = num1+num2
        print(f"The result of the sum is: {result}")

    elif op == 2:
        result = num1-num2
        print(f"The result of the substraction is: {result}")
    elif op == 3:
        result = num1*num2
        print(f"The result of the multipl is: {result}")
    elif op == 4:
        result = num1/num2
        print(f"The result of the division is: {result}")
    print("\n")
    print(f"{num1} is an even number") if num1 % 2 == 0 else print(f"{num1} is an odd number")  # se puede hacer todo en una linea de esta forma si la condicion no es muy compleja.
else:
    print("you've made an invalid selection")


def sumar(a, b):
    return a+b


my_dict = {1: sumar}

resultado = my_dict[op](num1, num2)

