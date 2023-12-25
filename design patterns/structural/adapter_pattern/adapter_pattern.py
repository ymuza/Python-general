"""This pattern allows you to convert the interface of a class into another interface.
It's usefull when you want to use an existing class that doesn't quite fit with the 
rest of your code, but you don't want to modify its source code."""


class ArgentinianSocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


class USASocket:

    @staticmethod
    def voltage():
        return 110

    @staticmethod
    def live():
        return 1

    @staticmethod
    def neutral():
        return -1


class Adapter(ArgentinianSocketInterface):

    def __init__(self, socket_type):
        self.socket = socket_type

    def voltage(self):
        return self.socket.voltage()

    def live(self):
        return self.socket.live()

    def neutral(self):
        return self.socket.neutral()

    def earth(self):
        return 0


if __name__ == '__main__':
    socket = USASocket()
    adapter = Adapter(socket)

    print(adapter.voltage())  # 110
    print(adapter.live())  # 1
    print(adapter.neutral())  # -1
    print(adapter.earth())  # 0
