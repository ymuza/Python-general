
# step 1, recursive case =>  f(n) = f(n-1) + f(n-2)

def fibonacci(n):  # n is the position , example => fibonacci number 20 is 6765.
    assert 0 <= n and int(n) == n, 'fibonacci number must be a positive integer.'
    if n in [0, 1]:  # step 2 => base case, stop criterion
      return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # step 1 => recursive case



print(fibonacci(20))