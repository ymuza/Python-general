try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1/number2)
except ZeroDivisionError as e:  # Es el mensaje default de python para divisiones por cero, y se guarda en e
    print("you can't divide a number by zero", e)  # cuando aparezca el mensaje de error, incluirá el ZeroDivisionError

except ValueError as e:  # mandamos que se imprima el valueError
    print("invalid Input")

except Exception as e:  # Exception maneja errores generales,
    print("something went wrong...", e)


finally:
    print("bye")