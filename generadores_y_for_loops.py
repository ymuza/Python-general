list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum1 = 0

for num in list1: #recorre todos los numeros en 'list'.
    sum1 = sum1+num

print(sum1)
print("\n")
for num in range(10):#for que recorre los numeros que hay en un generador range de 10 numeros (range(10) genera 10 numeros del 0 al 9).
    print("hello")#acá va a imprimir 10 veces hello porque toma como numero de veces a recorrer lo que indica range(10).
    #print(num)



for num in range(len(list1)): #el for recorre la cantidad de veces igual al numero de enteros de la lista.
    print("bye")

print("\n")

run_times = int(input("How many times you want it to run?: "))

for num in range(run_times):
    print(f"run: {num+1}") #le digo que recorra num+1 para que no empiece desde el 0 sino desde el 1.
