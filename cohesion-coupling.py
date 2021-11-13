"""
Dev Notes: Practice of Software Quality Metrics related concepts
    - Cohesion
    - Coupling
"""

import string
import random


class VehicleInfo:
	def __init__(self, brand: str, catalogue_price: int, electric: bool) -> None:
		self.brand: str = brand
		self.catalogue_price: int = catalogue_price
		self.electric: bool = electric

	def compute_tax_percentage(self) -> float:
		return 0.02 if self.electric else 0.05

	def compute_tax(self) -> float:
		tax_percentage: float = self.compute_tax_percentage()
		return self.catalogue_price * tax_percentage

	def print(self) -> None:
		print(f"Brand: {self.brand}")
		print(f"Payable Tax: {self.compute_tax()}")


class Vehicle:
	def __init__(self, id: str, license_plate: str, vehicle_info: VehicleInfo) -> None:
		self.id: str = id
		self.license_plate: str = license_plate
		self.info: VehicleInfo = vehicle_info

	def print(self) -> None:
		print(f"Id: {self.id}")
		print(f"License Plate: {self.license_plate}")
		self.info.print()


class VehicleRegistry:
	def __init__(self) -> None:
		self.vehicle_info: dict = {}
		self.add_vehicle_info(brand="Tesla Model 3", catalogue_price=60000, electric=True)
		self.add_vehicle_info(brand="Volkswagen ID3", catalogue_price=35000, electric=True)
		self.add_vehicle_info(brand="BMW 5", catalogue_price=5000, electric=False)
		self.add_vehicle_info(brand="Tesla Model Y", catalogue_price=5000, electric=True)

	def add_vehicle_info(self, brand: string, catalogue_price: int, electric: bool) -> None:
		self.vehicle_info[brand] = VehicleInfo(brand=brand, catalogue_price=catalogue_price, electric=electric)

	def generate_vehicle_id(self, lenght) -> str:
        	return ''.join(random.choices(string.ascii_uppercase, k=lenght))

	def generate_vehicle_license(self, id) -> str:
        	return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

	def create_vehicle(self, brand: str) -> Vehicle:
		vehicle_id: str = self.generate_vehicle_id(12)
		license_plate: str = self.generate_vehicle_license(vehicle_id)
		return Vehicle(
			id=vehicle_id,
			license_plate=license_plate,
			vehicle_info=self.vehicle_info[brand]
		)

class VehicleRegistrationUseCase:
	def __init__(self, vehicle_registry: VehicleRegistry()) -> None:
		self.registry: VehicleRegistry = vehicle_registry

	def register_vehicle(self, brand: str) -> Vehicle:
		return self.registry.create_vehicle(brand)

vehicle_registry: VehicleRegistry() = VehicleRegistry()
app = VehicleRegistrationUseCase(vehicle_registry=vehicle_registry)
vehicle: Vehicle = app.register_vehicle("BMW 5")
vehicle.print()
