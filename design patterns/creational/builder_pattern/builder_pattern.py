"""Good pattern to use when we need to create very complex objects, with many optional parameters 
or variations. In this pattern, the construction of an object is separated from its representation,
allowing us to create different representations of the object, with the same construction
process."""


class RPGCharacter:
    def __init__(self):
        self.__stats = None
        self.__gender = None
        self.__body = None

    def set_stats(self, stats):
        self.__stats = stats

    def set_gender(self, gender):
        self.__gender = gender

    def set_body(self, body):
        self.__body = body


class RPGCharacterBuilder:
    def __init__(self):
        self.__rpg_character = RPGCharacter()

    def set_stats(self, value):
        self.__rpg_character.set_stats(value)
        return self

    def set_gender(self, value):
        self.__rpg_character.set_gender(value)
        return self

    def set_body(self, value):
        self.__rpg_character.set_body(value)
        return self

    def get_rpg_character(self):
        return self.__rpg_character


builder = RPGCharacterBuilder()
builder.set_stats({'inteligence': '9', 'strength': '7', 'dexterity': '8'})\
       .set_gender('Male')\
       .set_body({'height': '1.90 m', 'weight': '86 kg'})

rpg_character = builder.get_rpg_character()
