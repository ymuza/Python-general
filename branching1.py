
#-----------------if/elif/else-----------------



result = 0



op = int(input("select an operation (1-sum, 2-subst, 3-multip, 4-div): "))

if op == 1 or op == 2 or op == 3 or op == 4:

    print("Enter a number: ")
    num1 = float(input())
    print("Enter a second number: ")
    num2 = float(input())

    if op == 1:
        result = num1+num2
        print(f"The result of the sum is: {result}")
    else:
      if op == 2:
        result=num1-num2
        print(f"The result of the substraction is: {result}")
      else:
          if op == 3:
             result = num1*num2
             print(f"The result of the multipl is: {result}")
          else:
              if op == 4:
                 result = num1/num2
                 print(f"The result of the division is: {result}")

else:
    print("you've made an invalid selection")
