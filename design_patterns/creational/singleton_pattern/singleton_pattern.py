"""In this pattern, there's only one instance by class, and you can access that instance
globaly. It's useful when you want to control the instantiation of a class, and ensure that
only one instance exists at any given time """


class SingletonError(RuntimeError):
    """Raised when something tries to create a second Singleton instance."""


class Singleton:
    """Allows only one instance. Use get_instance() instead of calling the constructor."""
    _instance = None

    def __init__(self):
        cls = type(self)
        # look in the class's own __dict__ so each subclass gets its own instance
        if cls.__dict__.get("_instance") is not None:
            raise SingletonError(f"{cls.__name__} cannot be instantiated multiple times!")
        cls._instance = self

    @classmethod
    def get_instance(cls, *args, **kwargs):
        """Return the single instance of cls, creating it (with args) the first time."""
        if cls.__dict__.get("_instance") is None:
            cls(*args, **kwargs)
        return cls._instance


class Database(Singleton):
    """Singleton subclass that holds shared data."""
    def __init__(self, data=None):
        super().__init__()
        self.data = data


def main():
    """Show that two get_instance() calls return the same object."""
    db1 = Database.get_instance()
    db2 = Database.get_instance()

    print(db1 is db2)  # True

    db1.data = {'name': 'Homer', 'age': 45}
    print(db2.data)  # {'name': 'Homer', 'age': 45}


if __name__ == '__main__':
    main()
