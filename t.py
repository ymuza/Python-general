class Suma:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def ecuacion(self, num3):
        num4 = num3 * (self.num1 + self.num2)
        return num4

    def multip4(self, num5):
        multip = 4 * self.ecuacion(3) * num5
        return multip


a = Suma(2, 2)
a.ecuacion(3)
a.multip4(6)
print(a.multip4(6))
