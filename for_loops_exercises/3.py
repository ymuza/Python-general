

def even_numbers():
    # EXERCISE 2: Filtering with Condition
    # Create a list of even numbers from 1 to 20

    even_numbers = [i for i in range(1, 21) if i % 2 == 0 ]

    return even_numbers




def upper_case():
    # EXERCISE 3: String Manipulation
    # Convert a list of names to uppercase
    name_list = ["carlos", "maria", "juan"]
    upper_case = [name.upper() for name in name_list]


    return upper_case


def even_odd():
    # EXERCISE 4: Conditional Expression (Ternary)
    # Create a list that contains "even" or "odd" for numbers 1-10
    even_odd = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
    print(f"Solution: {even_odd}")







# EXERCISE 10: Multiple Conditions
# Get numbers that are divisible by both 2 and 3 from range 1-30



print(even_numbers())

print(upper_case())

print(even_odd())