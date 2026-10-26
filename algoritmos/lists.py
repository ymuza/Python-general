"""In-place list rearrangement exercises (zeros, negatives, signs, parity)."""

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
    # partición estable: primero los negativos, después el resto, cada grupo en su orden original
    negatives = [v for v in list1 if v < 0]
    others = [v for v in list1 if v >= 0]
    print(negatives + others)


def move_specific_element_to_the_end(number, list1=None):
    """Move all occurrences of an element to the end, keeping the order of the rest.
    With list1 = [1, 3, 2, 3, 4, 3] and element 3, output should be: [1, 2, 4, 3, 3, 3]"""
    if list1 is None:
        list1 = [1, 3, 2, 3, 4, 3]
    if number not in list1:
        print("the number must be in the list.")
        return list1

    # partición estable: los que no son el número primero, luego todas las apariciones del número
    rest = [v for v in list1 if v != number]
    moved = [v for v in list1 if v == number]
    result = rest + moved
    print(result)
    return result


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
    primes = [v for v in list1 if is_prime(v)]
    non_primes = [v for v in list1 if not is_prime(v)]
    print(primes + non_primes)


def group_by_sign():
    """groups all positive numbers followed by all negative numbers while maintaining
     their relative order within each group. Output should be: [1, 3, 5, -2, -4, -6]"""
    list1 = [1, -2, 3, -4, 5, -6]
    # partición estable: positivos primero, negativos después
    positives = [v for v in list1 if v >= 0]
    negatives = [v for v in list1 if v < 0]
    print(positives + negatives)


def main():
    """Reads an option number and runs the matching exercise."""
    try:
        option = int(input("select an algorithm: "))
    except ValueError:
        print("please enter a valid number.")
        return

    if option == 1:
        zeroes_to_the_end()
    elif option == 2:
        negatives_to_the_front()
    elif option == 3:
        try:
            n = int(input("enter the number: "))
        except ValueError:
            print("please enter a valid number.")
            return
        move_specific_element_to_the_end(n)
    elif option == 4:
        separate_odd_from_even()
    elif option == 5:
        primes_to_the_front()
    elif option == 6:
        group_by_sign()
    else:
        print("unknown option.")


if __name__ == '__main__':
    main()
