"""This pattern allows us to define a one-to-many dependency between objects,
 so that when one object changes state, all its dependents are notified
 and updated automatically."""


class EmailProviderSource:
    def __init__(self, name: str):
        self.name = name
        self.users = []

    def add_user(self, user) -> None:
        self.users.append(user)

    def remove_user(self, user) -> None:
        self.users.remove(user)

    def notify_users(self, account_message: str) -> None:
        for user in self.users:
            user.update(self.name, account_message)


class EmailUser:
    def __init__(self, name: str):
        self.name = name

    def update(self, source_name: str, account_message: str) -> None:
        print(f"{self.name} received an account message from {source_name}: {account_message}")


if __name__ == '__main__':
    outlook = EmailProviderSource('outlook')
    gmail = EmailProviderSource('gmail')

    Ricardo = EmailUser('Ricardo Cataldi')
    Yamil = EmailUser('Yamil Muza')

    gmail.add_user(Ricardo)
    outlook.add_user(Yamil)

    gmail.notify_users('Security alert: logging from an unknown device')
    outlook.notify_users('Please buy microsft office 365')
