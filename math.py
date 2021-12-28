num_1 = "10"
num_2 = "20"

result = int("10") + int("10")  # Type Casting: convierte strings a enteros o floats (en este caso enteros).
print(result)

print("\n")
# ------------------------calculadora----------------------------------


print("Enter a number: ")
num1 = float(input())
print("Enter a second number: ")
num2 = float(input())
print("select an operation (1-sum, 2-subst, 3-multip, 4-div): ")
op = int(input())

if op == 1:
    suma = num1 + num2
    print(f"The result of the sum is: {suma}")

if op == 2:
    op = num1 - num2
    print(f"The result of the substraction is: {op}")

if op == 3:
    op = num1 * num2
    print(f"The result of the multipl is: {op}")

if op == 4:
    op = num1 / num2
    print(f"The result of the division is: {op}")

print("\n")
# -----------------------
a = int(100 / 3.3)

# mid=len(1)//2

print(a)
