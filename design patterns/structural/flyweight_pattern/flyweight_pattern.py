"""This pattern allows us  to share common state between multiple objects,
in order to save memory and improve performance. This pattern is useful when
you have a large number of objects that share the same data, and you want to
avoid creating new objects for each instance of the data. """


class Player:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class PlayerFactory:
    def __init__(self):
        self._players = {}

    def get_player(self, name, height):
        if name not in self._players:
            self._players[name] = Player(name, height)
        return self._players[name]


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players


if __name__ == '__main__':
    factory = PlayerFactory()

    player1 = factory.get_player("LeBron James", "6'9")
    player2 = factory.get_player("Anthony Davis", "6'10")
    player3 = factory.get_player("LeBron James", "6'9")

    team1 = Team("Los Angeles Lakers", [player1, player2])
    team2 = Team("Brooklyn Nets", [player1, player3])

    print(f"{player1.name} is on {team1.name}")
    print(f"{player2.name} is on {team1.name}")
    print(f"{player3.name} is on {team2.name}")
