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
    """writes fibonacci series up until n """
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
    """removes the element in certain position"""
    if position < 0 or position >= len(char_list):
        print("invalid position")
        return char_list
    else:
        char_to_remove = ''.join(char_list[position:position + 1])
        if char_to_remove in char_list:
            char_list.remove(char_to_remove)
        print(char_list)
    return char_list

def duplicates_in_list(element_list):
    """add the duplicates on a new list"""
    seen = []
    duplicates = []

    for i in element_list:
        if i not in seen:
            seen.append(i)
        else:
            duplicates.append(i)

    print("list: ", element_list)

    print("duplicates:", ','.join(map(str, duplicates)))



def longest_unique_substring(string):
    """"""
    if not string:
        return 0
    max_length = 0
    start = 0
    char_index_map = {}



def two_sum(nums, t):
    """Given a list of integers and a target,
       return the indices of the two numbers that add up to the target."""
    seen = {}

    nums = nums
    target = t

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return ""

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_to_the_front():
    """move all prime numbers to the front of the list while maintaining
    the relative order of non-prime numbers. Output should be: [3, 5, 11, 10, 8, 15]"""
    list1 = [10, 3, 5, 8, 11, 15]
    primes = []
    non_primes = []

    for num in list1:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)

    return primes + non_primes


def zeroes_to_the_end():
    """move 0 to the end of the list"""

    list1 = [10, 0, 20, 0, 40, 60]

    position = 0
    for i in list1:
        if i != 0:
            list1[position] = i
            position += 1

    while position < len(list1):
        list1[position] = 0
        position += 1
    print(list1)


def main():
    print("1 - Check if palindrome")
    print("2 - Calculate factorial")
    print("3 - Find max")
    print("4 - Binary search")
    print("5 - FizzBuzz")
    print("6 - Fibonacci series")
    print("7 - Remove element by position")
    print("8 - Find duplicated items in list")
    print("9 - Find longest substring without repeating characters")
    print("10 - Two sum")
    print("11 - check if a number is prime")
    print("12 - Primes to the front of the list")
    print("13 - Move zeroes to the end")
    print("14 - ")
    print("_______________________________________________")

    try:
        choice = int(input("Choose an algorithm: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    match choice:
        case 1:
            s = input("Enter a string: ")
            print(is_palindrome(s))

        case 2:
            n = int(input("Enter a number: "))
            print(factorial(n))

        case 3:
            items = list(map(int, input("Enter numbers separated by space: ").split()))
            print(find_max(items))

        case 4:
            arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))
            target = int(input("Enter the target number: "))
            print(binary_search(arr, target))

        case 5:
            n = int(input("Enter a number: "))
            print(fizzbuzz(n))

        case 6:
            n = int(input("Enter number of terms: "))
            print(fibonacci_series(n))

        case 7:
            items = input("Enter characters separated by space: ").split()
            pos = int(input("Enter position to remove: "))
            print(remove_element_by_position(pos, items))

        case 8:
            items = input("Enter elements separated by space: ").split()
            print(duplicates_in_list(items))

        case 9:
            s = input("Enter a string: ")
            print(longest_unique_substring(s))

        case 10:
            number_list = [2, 4, 3, 6, 10]
            target = 8
            print(two_sum(number_list, target))

        case 11:
            n = 2
            is_prime(n)

        case 12:
           print(primes_to_the_front())

        case 13:
            zeroes_to_the_end()

        case _:
                print("Invalid choice.")


main()

