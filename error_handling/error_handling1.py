a = 5

b = 0

try:
    print("resource open")  # simulo que abro un recurso x
    print(a/b)
except Exception as e:  # except se usa para señalar las excepciones al correcto funcionamiento
    print("You can't divide a number by zero", e)

finally:  # finally indica que no importa lo que pase, si tira o no error, lo que sigue se va a ejecutar
    print("resource closed")  # en este ejemplo, siempre que se deja de usar un recurso hay que cerrarlo/cortarlo

print("\n")









