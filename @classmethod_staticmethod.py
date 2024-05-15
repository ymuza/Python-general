class Student:
    
    school = 'papachers'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3) / 3
    
    @classmethod  # si quiero usar una variable de clase, en este caso school, tengo que invocarla con 'cls' , pero para poder usar cls debo agregar @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod  # este metodo se usa cuando no queres que este metodo este relacionado con los objetos de clase, o de instancia.
    def info():
        print("this is a student class")


s1 = Student(34, 67, 32)
s2 = Student(89, 32, 142)
    
    
print(s2.avg())
print(s2.getschool())
Student.info()
