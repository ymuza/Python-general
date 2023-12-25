
def test(num1, num2):

    if num1 < 200:
        print(num2)
        test(num1+12, num2+3)


test(15, 15)

