"""Ejemplo de try/except/finally al dividir por cero."""

A = 5

B = 0

try:
    print("resource open")  # simulo que abro un recurso x
    print(A/B)
# except se usa para señalar las excepciones al correcto funcionamiento
except ZeroDivisionError as e:
    print("You can't divide a number by zero", e)

# finally indica que no importa lo que pase, si tira o no error, lo que sigue se va a ejecutar
finally:
    # en este ejemplo, siempre que se deja de usar un recurso hay que cerrarlo/cortarlo
    print("resource closed")

print()
