"""The mediator pattern is used to communicate between objects through a mediator object.
In this case, we have a mediator which receives a message from a sender and delivers it
to the other objects"""

class Mediator:
    """keeps the participants and forwards messages between them"""
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        """registers a person so they can receive messages"""
        self.persons.append(person)

    def broadcasted_messages(self, sender, message):
        """delivers the message to everyone except the sender"""
        for person in self.persons:
            if person != sender:
                person.receive(sender, message)


class Person:
    """participant that only talks to the mediator, never to other persons directly"""
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def __repr__(self):
        return self.name

    def send(self, message):
        """sends a message through the mediator"""
        self.mediator.broadcasted_messages(self, message)

    def receive(self, sender, message):
        print(f"Received message from {sender}: {message}")

def main():
    """creates two persons and makes them exchange messages through the mediator"""
    chat_mediator = Mediator()

    person1 = Person("Alice", chat_mediator)
    person2 = Person("Bob", chat_mediator)

    chat_mediator.add_person(person1)
    chat_mediator.add_person(person2)

    person1.send("Hello, ")
    person2.send("Hey there!")


if __name__ == "__main__":
    main()
