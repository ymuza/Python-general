# Bubble sort algorithm:


def bs(lista):  # a = name of list
    b = len(lista) - 1  # minus 1 because we always compare 2 adjacent values

    for x in range(b):
        for y in range(b - x):
            if lista[y] > lista[y + 1]:
                lista[y], lista[y + 1] = lista[y + 1], lista[y]
    return a


bs(list)
  # -----------------------------------------------------
  # star triangle


def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))


pyfunc(9)

  #  -----------------------------------------------------
# fibonacci series

# Enter number of terms needed                   #0,1,1,2,3,5....
a = int(input("Enter the terms"))
f = 0                                         #first element of series
s = 1                                         #second element of series
if a <= 0:
    print("The requested series is", f)
else:
    print(f, s, end=" ")
    for x in range(2, a):
        next = f+s
        print(next, end=" ")
        f = s
        s = next
  # -----------------------------------------------------------

# check if a number is prime
a = int(input("enter number"))
if a > 1:
    for x in range(2, a):
        if(a % x) == 0:
            print("not prime")
            break
    else:
        print("Prime")
else:
    print("not prime")
# --------------------------------------------------------
# check if a secuence is palindrome
a = input("enter sequence")
b = a[::-1]
if a == b:
    print("palindrome")
else:
    print("Not a Palindrome")




"""
op = int(input("select a program: "))
l = [32, 5, 3, 6, 7, 54, 87]
if op == 1:

    pyfunc(l)
elif op== 2:
"""
