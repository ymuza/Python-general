class Test:

    def __init__(self):
        self.__name = "ttt"

    def get_variable(self):
        return self.__name

    def modify_variable(self):
        self.__name = "fff"
        return self.__name
class Rrrr:
    @staticmethod
    def access():
        test = Test()
        test.__name = ""


test = Test()
print(test.get_variable())
