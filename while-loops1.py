from random import randint

print("type a number: ")
num = int(input())
while num < 12:
    print(num)
    num = num + 1

print("\n")

list1 = [randint(1, 100) for num in range(1000)]
f = 0

num_to_search = 23

while f < len(list1):
    if list1[f] == num_to_search:
        print(f"{num_to_search} found at index {f}")
    f = f + 1

print("\n")

availableCandy = 10

x = int(input("how many candies do you want?: "))

i: int = 1
while i <= x:
    if i > 10:
        print(f"there are just {x} candies")
        break
    print("candy")
    i += 1

