"""This pattern allows us to define a one-to-many dependency between objects,
 so that when one object changes state, all its dependents are notified
 and updated automatically."""


class EmailProviderSource:
    """the subject: keeps a list of users and notifies all of them"""
    def __init__(self, name: str):
        self.name = name
        self.users = []

    def add_user(self, user) -> None:
        self.users.append(user)

    def remove_user(self, user) -> None:
        self.users.remove(user)

    def notify_users(self, account_message: str) -> None:
        """sends the message to every subscribed user"""
        for user in self.users:
            user.update(self.name, account_message)


class EmailUser:
    """the observer: gets notified by the providers it is subscribed to"""
    def __init__(self, name: str):
        self.name = name

    def update(self, source_name: str, account_message: str) -> None:
        """called by the subject when there is a new message"""
        print(f"{self.name} received an account message from {source_name}: {account_message}")


if __name__ == '__main__':
    outlook = EmailProviderSource('outlook')
    gmail = EmailProviderSource('gmail')

    ricardo = EmailUser('Ricardo Cataldi')
    yamil = EmailUser('Yamil Muza')

    gmail.add_user(ricardo)
    outlook.add_user(yamil)

    gmail.notify_users('Security alert: login from an unknown device')
    outlook.notify_users('Please buy microsoft office 365')
