"""How to write a recursion function in 3 steps?
---------------------------------------------
1 - Identify the recursive case - the flow
2 - Base case - the stopping criterion
3 - Unintentional case - the constraint

1 - identify the factorial function
 . factorial function => n! = n *(n-1) * (n-2)*....*2 * 1
 . this => (n-1) * (n-2)*....*2 * 1 , can be expressed as (n-1)!
 . So , the factorial function (which would be the recursive case) is n! = n * (n-1)!"""

def factorial(n):
 if n < 0  or not isinstance(n, int):  # this is the step 3, the unintentional constraint
     raise ValueError('n must be a positive integer')
 else:
    if n in [0, 1]:  # this is the 2 step, the base case => the stopping criterion (0!=1, 1!=1)
        return 1
    else:
        return n * factorial(n-1)  # this is the function for the first step, the recursive case  n! = n * (n-1)

print(factorial(4))