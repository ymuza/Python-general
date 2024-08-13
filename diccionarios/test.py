def describe_value(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3 | 4 | 5:  # Matches 3, 4, or 5
            return "Three, Four, or Five"
        case _ if value < 0:  # Matches any negative value
            return "Negative number"
        case _ if value > 5:  # Matches any value greater than 5
            return "Greater than Five"
        case _:
            return "Something else"

# Examples of calling the function
print(describe_value(1))  # Output: One
print(describe_value(4))  # Output: Three, Four, or Five
print(describe_value(-3))  # Output: Negative number
print(describe_value(10))  # Output: Greater than Five
print(describe_value(0))  # Output: Something else
