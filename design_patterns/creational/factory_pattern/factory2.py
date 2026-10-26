"""Simple Factory: a single class with a static factory method decides which concrete
Sports object to create from a name. The client only knows the Sports interface and
never instantiates Football or Basketball directly.
This is the simplest form of factory; there is no subclass delegation (that would be
the Factory Method pattern)."""


class Sports:
    """Base interface for the sports the factory can create."""
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
        """Return the Sports subclass for the given name. Raises ValueError if unknown."""
        if sport == "basketball":
            return Basketball()
        if sport == "football":
            return Football()
        raise ValueError('invalid sport')


if __name__ == "__main__":
    basketball = SportsFactory.create_sport('basketball')
    football = SportsFactory.create_sport('football')

    football.play()  # kicking the ball
    basketball.play()  # shooting 3-pointers
