from random import randint

# generar 100 enteros aleatorios entre el 1 y el 100.

list1 = [randint(1, 100) for num in range(100)]  # 'randint' genera enteros aleatorios entre el 1 y el 100 .
print(list1)

print("\n")

list1 = [num ** 2 for num in range(
    100)]  # la lista se forma con el cuadrado de los numeros del 1 al 100,y dentro de la lista recorro con 'for'.
print(list1)

print("\n")

list1 = [randint(1, 100) for num in range(100)]
print(list1)

print(list(range(6)))  # imprime en forma de lista los elementos del 0 al 5 (usando el generador 'range').
print("\n")

my_dictionary = {'height': '2.04 m', 'weight': '115 kg', 'age': 24}
print(my_dictionary)

print("\n")

for key, value in my_dictionary.items():  # recorre todas las keys de mi_dictionary.
    print(f"key is:{key}, and value is {value}")

print("\n")


for x in range(20, 23, 5):  # recorre el rango entre 20 y 23, de a 5. Como se pasa el resultado es 20
    print(x)


print(" ")

print(" ")
start = 25
end = 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % 2 != 0:
                print(i)





