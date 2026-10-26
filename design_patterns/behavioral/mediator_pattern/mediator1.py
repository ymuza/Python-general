"""The mediator pattern is used to communicate between objects through a mediator object. In this case, we have a
 mediator which recieves a messaje from a sender and delivers it to other object"""

class Mediator:
    def __init__(self):
        self.persons = set()

    def add_person(self, person):
        self.persons.add(person)

    def broadcasted_messages(self, sender, message):
        for person in self.persons:
            if person != sender:
                person.receive(sender, message)


class Person:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.broadcasted_messages(self, message)

    def receive(self, sender, message):
        print(f"Received message from {sender}: {message}")

mediator = Mediator()

person1 = Person(mediator)
person2 = Person(mediator)

mediator.add_person(person1)
mediator.add_person(person2)

person1.send("Hello, ")
person2.send("Hey there!")
