class MyClass:
    def __init__(self, value):
        self.__value = value  # private attribute

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()  # calling private method within the class

# Create an instance of MyClass
obj = MyClass(42)

# Accessing public method
obj.__private_method()

# Attempting to access private method directly will result in an error
# Uncommenting the line below will raise an AttributeError
# obj.__private_method()



test = obj.public_method()