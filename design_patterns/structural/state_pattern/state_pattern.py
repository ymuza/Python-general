"""State pattern: an object changes its behavior when its internal state changes.
RadioStation (the context) holds a state object and delegates change_state() to it.
Each state performs its action and then sets the next state on the radio, so calling
radio.change_state() repeatedly cycles OFF -> ON -> LOUDER -> QUIETER -> OFF..."""

from abc import ABC, abstractmethod


class InternalState(ABC):
    """Interface for the states the radio can be in."""
    @abstractmethod
    def change_state(self, radio: "RadioStation") -> None:
        """Perform this state's action and move the radio to the next state."""


class TurnedOff(InternalState):
    """State in which the radio is off."""
    def change_state(self, radio):
        print("Turning ON the device!!!")
        radio.set_state(TurnedOn())


class TurnedOn(InternalState):
    """State in which the radio is on."""
    def change_state(self, radio):
        print("Increasing volume by 10 !!!")
        radio.set_state(IncreasedVolume())


class IncreasedVolume(InternalState):
    """State in which the volume was raised."""
    def change_state(self, radio):
        print("Decreasing volume by 10 !!!")
        radio.set_state(DecreasedVolume())


class DecreasedVolume(InternalState):
    """State in which the volume was lowered."""
    def change_state(self, radio):
        print("Turning OFF the device!!!")
        radio.set_state(TurnedOff())


class RadioStation:
    """Context: holds the current state and delegates change_state() to it."""
    def __init__(self):
        self.state: InternalState = TurnedOff()

    def get_state(self) -> str:
        return type(self.state).__name__

    def set_state(self, state: InternalState) -> None:
        self.state = state

    def change_state(self) -> None:
        self.state.change_state(self)


if __name__ == "__main__":
    radio = RadioStation()
    print(f"The radio's internal state is currently: {radio.get_state()}")

    for _ in range(5):
        radio.change_state()
        print(f"The radio's internal state is currently: {radio.get_state()}")
