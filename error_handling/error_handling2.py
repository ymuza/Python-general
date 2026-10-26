"""Manejo de varias excepciones (ZeroDivisionError, ValueError, Exception) con finally."""

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1/number2)
# Es el mensaje default de python para divisiones por cero, y se guarda en e
except ZeroDivisionError as e:
    # cuando aparezca el mensaje de error, incluirá el ZeroDivisionError
    print("you can't divide a number by zero", e)

except ValueError:  # mandamos que se imprima el valueError
    print("invalid Input")

except Exception as e:  # pylint: disable=broad-exception-caught  # Exception maneja errores generales,
    print("something went wrong...", e)


finally:
    print("bye")
