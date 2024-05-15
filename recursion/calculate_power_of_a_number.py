"""calculate power of a number using recursion"""

""" 
step 1: Recursive case - the flow
------------------------------------
# x^n  = x^n * x^n * x^n...(n times)..* x

# x^n = x * x^n-1
"""
######################################################

"""
step 2: base case - the stopping criterion 
********************************************

n = 0

"""
######################################################

def power_of_a_number(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power_of_a_number(base, exponent + 1)  # +1 for it to get to 0
    elif type(exponent) is float:
        raise ValueError("exponent must be an integer number")
    else:
        return base * power_of_a_number(base , exponent-1)

print(power_of_a_number(6,-1))