from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta):
	@abstractmethod
	def change_state(self):
		pass

class TurnedOn(InternalState):
	def change_state(self):
		print("Turning ON the device!!!")
		return "ON"

class TurnedOff(InternalState):
	def change_state(self):
		print("Turning OFF the device!!!")
		return "OFF"


class IncreaseVolume(InternalState):
	def change_state(self):
		print("Increasing volume by 10 !!!")
		return "+10"

class DecreaseVolume(InternalState):
	def change_state(self):
		print("Decreasing volume by 10 !!!")
		return "-10"



class RadioStation(InternalState):
	def __init__(self):
		self.state = None

	def get_state(self):
		return self.state

	def set_state(self, status):
		self.state = status

	def change_state(self):
		self.state = self.state.change_state()

Radio = RadioStation()
print('The radios internal state is currently: {}'.format(Radio.get_state()))

ON = TurnedOn()
OFF = TurnedOff()

Louder = IncreaseVolume()
Lower = DecreaseVolume()

print("Turning on the radio!")
Radio.set_state(ON)
Radio.change_state()
print('The radios internal state is currently: {}'.format(Radio.get_state()))

print("Turning off the radio!")
Radio.set_state(OFF)
Radio.change_state()
print('The radios internal state is currently: {}'.format(Radio.get_state()))

print("Increasing the volume!")
Radio.set_state(Louder)
Radio.change_state()
print('The radios internal state is currently: {}'.format(Radio.get_state()))