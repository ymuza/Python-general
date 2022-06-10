#  lets say it takes 1 second per loop

#  1 second to execute =>  array = [1]
#  5 seconds to execute =>  array = [1, 2, 3, 4, 5]
#  10 seconds to execute =>  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  20 seconds to execute =>  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

"""
- print every number in the array
- count the frequency of each number
- find an element in a sorted array
- sort an array
"""
array = [1, 2, 3, 4, 5]
# COMPLETAR!!!!!!
# O(n) time complexity (linear time complexity) , where n is the number of elements in te array
for i in range(len(array)):
    print("num:", array[i])

# O(n^2) time complexity
for i in range(len(array)):
    print("num", array[i])
    for j in range(len(array)):
        print("num", array[j])


for i in range(len(array)):
    numCount = 1
    for j in range(len(array)):
        if array[i] == array[j] and i != j:
            numCount += 1

