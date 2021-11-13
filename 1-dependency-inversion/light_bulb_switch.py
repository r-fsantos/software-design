#!/usr/bin/env python

"""
Dev Notes: This file implements some code to practice
	- Interfaces
	- Dependency inversion
"""
from abc import ABC, abstractmethod


class Switchable(ABC):
	@abstractmethod
	def turn_on(self) -> None:
		pass

	@abstractmethod
	def turn_off(self) -> None:
		pass


class LightBulb(Switchable):
	def __init__(self) -> None:
		pass

	def turn_on(self) -> None:
		print("LightBulb: turned on...")

	def turn_off(self) -> None:
		print("LightBulb: turned off...")


class ElectricPowerSwitch:
	def __init__(self, switchable: Switchable) -> None:
		self.switchable: Switchable = switchable
		self.on: bool = False

	def press(self) -> None:
		if self.on:
			self.switchable.turn_off()
			self.on = False
		else:
			self.switchable.turn_on()
			self.on = True


if __name__ == '__main__':
	light_bulb: LightBulb = LightBulb() 
	electric_power_switch: ElectricPowerSwitch = ElectricPowerSwitch(switchable=light_bulb)
	electric_power_switch.press()
	electric_power_switch.press()
	electric_power_switch.press()
	electric_power_switch.press()	
