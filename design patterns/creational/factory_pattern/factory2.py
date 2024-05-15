"""To test the creational design patterns, we'll use in this example, the factory_pattern pattern.
The factory_pattern pattern provides an interface for creating objects in a super class, but allows
subclasses to alter the type of objects that will be created. This pattern is used when we
have to crate objects of similar type, or the object creation is very complex.
The Factory Design Pattern defines an interface or abstract class with a method or set of
methods that create an object, but the exact type of object is not specified in the interface.
The responsibility of creating the object is delegated to subclasses which implement the interface
and provide concrete implementations for the creation methods."""


class Sports:
    def play(self):
        pass


class Football(Sports):
    """class that implements the football interface """
    def play(self):
        print("kicking the ball")


class Basketball(Sports):
    """class that implements the basketball interface """
    def play(self):
        print("shooting 3-pointers")


class SportsFactory:
    """# Factory class that creates the objects"""
    @staticmethod
    def create_sport(sport):
        if sport == "basketball":
            return Basketball()
        elif sport == "football":
            return Football()
        else:
            raise ValueError('invalid sport')


factory = SportsFactory()
basketball = factory.create_sport('basketball')
football = factory.create_sport('football')

football.play()  # playing football
basketball.play()  # playing basketball
