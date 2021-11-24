
from randoms import randint
from randoms import ascii_lowercase
  # generar 100 enteros aleatorios entre el 1 y el 100.

list1 = [randint(1,100) for num in range(100)]  # 'randint' genera enteros aleatorios entre el 1 y el 100 .
print(list1)

print("\n")

list1 = [num**2 for num in range(100)]  # la lista se forma con el cuadrado de los numeros del 1 al 100,y dentro de la lista recorro con 'for'.
print(list1)

print("\n")

list1 = [randint(1,100) for num in range(100)]
print(list1)


print(list(range(6)))  # imprime en forma de lista los elementos del 0 al 5 (usando el generador 'range').
print("\n")

my_dictionary = {'height':'2.04 m','weight':'115 kg','age':24}
print(my_dictionary)

print("\n")

for key, value in my_dictionary.items():  # recorre todas las keys de mi_dictionary.
    print(f"key is:{key}, and value is {value}")


print("\n")
