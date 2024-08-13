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


def negatives_to_the_front():
    """move negatives to the front . Output should be: [-2, -4, -6, 1, 3, 5]"""
    list1 = [1, -2, 3, -4, 5, -6]
    position = 0  # This pointer will track the position of the last negative number

    for i in range(len(list1)):
        if list1[i] < 0:
            temp = list1[i]
            list1[i] = list1[position]
            list1[position] = temp
            position += 1
    print(list1)


def move_specific_element_to_the_end(number):
    """Move Specific Element to the End. If element is 3, Output should be: [1, 2, 4, 3, 3, 3]"""
    list1 = [5, 3, 43, 2, 4, 19]
    n = number
    if n not in list1:
        print("the number must be in the list.")
        return

    for i in range(len(list1)):
        if list1[i] == n:
            temp = list1[-1]
            list1[-1] = list1[i]
            list1[i] = temp
            break

    print(list1)


def separate_odd_from_even():
    """Write a function that segregates even and odd numbers,
    placing all even numbers first and odd numbers afterward,
     maintaining their relative order. Output should be: [2, 4, 6, 1, 3, 5]"""
    list1 = [1, 2, 3, 4, 5, 6]
    odds = []
    even = []
    for i in list1:
        if i % 2 == 0:
            even.append(i)
        else:
            odds.append(i)

    print(even + odds)


def primes_to_the_front():
    """move all prime numbers to the front of the list while maintaining
    the relative order of non-prime numbers. Output should be: [3, 5, 11, 10, 8, 15]"""
    list1 = [10, 3, 5, 8, 11, 15]


def group_by_sign():
    """groups all positive numbers followed by all negative numbers while maintaining
     their relative order within each group. Output should be: [1, 3, 5, -2, -4, -6]"""
    list1 = [1, -2, 3, -4, 5, -6]
    next_positive_index = 0

    n = len(list1)

    for i in range(n):
        if list1[i] >= 0:
            if i != next_positive_index:
                # Swap the elements at indices next_positive and i
                temp = list1[next_positive_index]
                list1[next_positive_index] = list1[i]
                list1[i] = temp
            next_positive_index += 1
    print(list1)


def main():
    option = int(input("select an algorithm: "))

    if option == 1:
        zeroes_to_the_end()
    elif option == 2:
        negatives_to_the_front()
    elif option == 3:
        n = int(input("enter the number: "))
        move_specific_element_to_the_end(n)
    elif option == 4:
        separate_odd_from_even()
    elif option == 5:
        primes_to_the_front()
    elif option == 6:
        group_by_sign()


if __name__ == '__main__':
    main()
