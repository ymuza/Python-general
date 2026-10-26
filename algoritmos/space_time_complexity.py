#  lets say it takes 1 second per loop

#  1 second to execute =>  array = [1]
#  5 seconds to execute =>  array = [1, 2, 3, 4, 5]
#  10 seconds to execute =>  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  20 seconds to execute =>  array = [1, 2, 3, ..., 20]

"""
- print every number in the array
- count the frequency of each number
- find an element in a sorted array
- sort an array
"""
array = [1, 2, 3, 4, 5]
# COMPLETAR!!!!!!
# O(n) time complexity (linear time complexity) , where n is the number of elements in te array
for num in array:
    print("num:", num)

# O(n^2) time complexity
for num in array:
    print("num", num)
    for other in array:
        print("num", other)


# O(n^2): count the frequency of each number
for i, num in enumerate(array):
    num_count = 1
    for j, other in enumerate(array):
        if num == other and i != j:
            num_count += 1
    print("num", num, "count:", num_count)
