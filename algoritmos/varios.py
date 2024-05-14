def is_palindrome(s):
    """checks if a string is a palindrome"""
    return s == s[::-1]


def factorial(n):
    """Write a function to calculate the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def find_max(lst):
    """function to find the maximum element in a list"""
    if not lst:
        return None
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem


def binary_search(array, target):
    """function to perform a binary search on a sorted list."""
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def fizzbuzz(n):
    """function to print numbers from 1 to n,
    but for multiples of 3 print "Fizz" instead of the number,
     and for multiples of 5 print "Buzz".
     For numbers which are multiples of both 3 and 5, print "FizzBuzz"""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fibonacci_series(n):
    if n <= 0:
        print(f"the series is: {n}")
    else:
        first = 0
        second = 1

        for i in range(0, n):
            next_number = first + second
            first = second
            second = next_number
            print(next_number)


def remove_element_by_position(position, char_list):
    if position < 0 or position >= len(char_list):
        print("invalid position")
        return char_list
    else:
        char_to_remove = ''.join(char_list[position:position + 1])
        if char_to_remove in char_list:
            char_list.remove(char_to_remove)
        print(char_list)


choice = int(input("choose an algorithm: "))

if choice == 1:
    print(is_palindrome("radar"))

elif choice == 2:
    print(factorial(5))

elif choice == 3:
    print(find_max([1, 5, 3, 9, 2]))

elif choice == 4:
    test_list = [2, 3, 4, 10, 40]
    target_number = 10
    print(binary_search(test_list, target_number))

elif choice == 5:
    print(fizzbuzz(15))

elif choice == 6:
    fibonacci_series(10)

elif choice == 7:
    character_list = ['a', 'b', 'c', 'd']
    pos = 1
    remove_element_by_position(pos, character_list)
