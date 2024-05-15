"""In this pattern, there's only one instance by class, and you can access that instance
globaly. It's useful when you want to control the instantiation of a class, and ensure that
only one instance exists at any given time """


class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton class cannot be instantiated multiple times!")
        else:
            Singleton.__instance = self

    @classmethod
    def get_instance(cls):
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


class Database(Singleton):
    def __init__(self, data):
        super().__init__()
        self.data = data


if __name__ == '__main__':
    db1 = Database.get_instance()
    db2 = Database.get_instance()

    print(db1 is db2)  # True

    db1.data = {'name': 'Homer', 'age': 45}
    print(db2.data)  # {'name': 'Homer', 'age': 45}
