"""This pattern allows us to encapsulate a request as an object,
thereby letting you parameterize clients with different requests,
 queue or log requests, and support undoable operations."""


class Television:
    def __init__(self):
        self.channel = 1
        self.volume = 50

    def change_channel(self, channel: int) -> None:
        self.channel = channel
        print(f"Changed channel to {self.channel}")

    def adjust_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"Adjusted volume to {self.volume}")


class Command:
    def execute(self) -> None:
        pass


class ChangeChannelCommand(Command):
    def __init__(self, tv: Television, channel: int):
        self.television = tv
        self.channel = channel

    def execute(self) -> None:
        self.television.change_channel(self.channel)


class AdjustVolumeCommand(Command):
    def __init__(self, tv: Television, volume: int):
        self.television = tv
        self.volume = volume

    def execute(self) -> None:
        self.television.adjust_volume(self.volume)


class RemoteControl:
    def __init__(self, tv: Television):
        self.television = tv
        self.commands = {}

    def set_command(self, button: str, command: Command) -> None:
        self.commands[button] = command

    def press_button(self, button: str) -> None:
        command = self.commands.get(button)
        if command:
            command.execute()


if __name__ == '__main__':
    television = Television()
    remote_control = RemoteControl(television)

    change_channel_command_1 = ChangeChannelCommand(television, 1)
    change_channel_command_2 = ChangeChannelCommand(television, 2)
    adjust_volume_command_1 = AdjustVolumeCommand(television, 30)
    adjust_volume_command_2 = AdjustVolumeCommand(television, 60)

    remote_control.set_command('button_1', change_channel_command_1)
    remote_control.set_command('button_2', change_channel_command_2)
    remote_control.set_command('button_3', adjust_volume_command_1)
    remote_control.set_command('button_4', adjust_volume_command_2)

    remote_control.press_button('button_1')
    remote_control.press_button('button_3')
    remote_control.press_button('button_2')
    remote_control.press_button('button_4')
