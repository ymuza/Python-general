my_list = [4, 5, 9, 90, 8, 9, 7, 65, 4444, 777, 1000]

my_list.append(10)#append agrega un elemento a la lista.
print(my_list)

my_list2 = ["aaa,bbb,eee"]
my_list3 = [56, 70, 80]
my_list4 = ["ddd,fff,ccc"]
my_list.extend(my_list3) #extiende o fusiona en este caso 2 listas.
print(my_list)
print("\n")
print(my_list2)

my_list2.extend(my_list4)
print(my_list2)

reversed_mylist = my_list[::-1]
print(reversed_mylist)
