class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # 'other' puede llamarse de otro nombre tambien
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s4 = Student(m1, m2)
        return s4

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2  # es lo mismo que hacer => Student.__add__(s1, s2) ,  donde s1 es 'self', y s2 es 'other'

s4 = s1 * s2

print("suma")
print(s3.m1)
print(s3.m2)

print("\n")

print("multiplicación")
print(s4.m1)
print(s4.m2)

if s1 > s2:
    print("s1 es mayor")
else:
    print("s2 es mayor")
