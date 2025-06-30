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


def move_specific_element_to_the_end():
    """Move Specific Element to the End. If element is 3, Output should be: [1, 2, 4, 3, 3, 3]"""
    list1 = [3, 1, 3, 2, 4, 3]


def separate_odd_from_even():
    """SWrite a function that segregates even and odd numbers,
    placing all even numbers first and odd numbers afterward,
     maintaining their relative order. Output should be: [2, 4, 6, 1, 3, 5]"""
    list1 = [1, 2, 3, 4, 5, 6]


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



def group_by_sign():
    """groups all positive numbers followed by all negative numbers while maintaining
     their relative order within each group. Output should be: [1, 3, 5, -2, -4, -6]"""
    list1 = [1, -2, 3, -4, 5, -6]





def two_sum():
    """Given a list of integers and a target,
       return the indices of the two numbers that add up to the target."""
    seen = {}

    nums = [2, 3, 4, 6, 10]
    target = 10

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return ""


def main():


    algorithms = {
                  1: zeroes_to_the_end,
                  2: negatives_to_the_front,
                  3: move_specific_element_to_the_end,
                  4: separate_odd_from_even,
                  5: primes_to_the_front,
                  6: group_by_sign,
        7:two_sum
                  }

    option = int(input("select an algorithm: "))
    algorithm = algorithms.get(option)
    if algorithm:
        algorithm()
    else:
        print("invalid option. Please select a valid algorithm.")


# if __name__ == '__main__':
#     main()

main()