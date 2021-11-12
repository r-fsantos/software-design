"""
Dev Notes: Practice of Software Quality Metrics related concepts
    - Cohesion
    - Coupling
"""

import string
import random


class VehicleInfo:
	def __init__(self, brand: str, catalogue_price: int, electric: bool):
		self.brand: str = brand
		self.catalogue_price: int = catalogue_price
		self.electric: bool = electric


class Vehicle:
	def __init__(self, id: str, license_plate: str, vehicle_info: VehicleInfo):
		self.id: str = id
		self.license_plate: str = license_plate
		self.info: VehicleInfo = vehicle_info


class VehicleRegistry:
	"""
	Dev Notes:
		- Add a constructor method, defining the following attributes: lenght, id, vehicle license. This are the attributes of the vehicle.
		- Then decouple all methods.
	"""
	def __init__(self):
		self.vehicle_info: dict = {}
		self.add_vehicle_info(brand="Tesla Model 3", catalogue_price=60000, electric=True)
		self.add_vehicle_info(brand="Volkswagen ID3", catalogue_price=35000, electric=True)
		self.add_vehicle_info(brand="BMW 5", catalogue_price=5000, electric=False)
		self.add_vehicle_info(brand="Tesla Model Y", catalogue_price=5000, electric=True)

	def add_vehicle_info(self, brand: string, catalogue_price: int, electric: bool) -> None:
		self.vehicle_info[brand]: VehicleInfo = VehicleInfo(brand=brand, catalogue_price=catalogue_price, electric=electric)

	def generate_vehicle_id(self, lenght) -> str:
        	return ''.join(random.choices(string.ascii_uppercase, k=lenght))

	def generate_vehicle_license(self, id) -> str:
        	return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

	def create_vehicle(self, brand: str):
		vehicle_id: str = self.generate_vehicle_id(12)
		license_plate: str = self.generate_vehicle_license(vehicle_id)
		return Vehicle(
			id=vehicle_id,
			license_plate=license_plate,
			vehicle_info=self.vehicle_info[brand]
		)

class Application:
	def register_vehicle(self, brand: str) -> None:
		# Creates a registry instance
		# TODO: Remove this coupling between Application and VehicleRegistry
		registry: VehicleRegistry = VehicleRegistry()
		
		vehicle: Vehicle = registry.create_vehicle(brand)

		# Computes the catalogue price
		# TODO: Remove Coupling between data
		#  catalogue_price and brands...
		#  Data it is not stored logically, 
		#  they need to be detached from each other
		catalogue_price: int = 0
		if brand == "Tesla Model 3":
		    catalogue_price = 60000
		elif brand == "Volkswagen ID3":
		    catalogue_price = 35000
		elif brand == "BMW 5":
		    catalogue_price = 45000

		# Computes the tax percentage (default 5% og the catalogue price,
		# except for eletric cars, where it is 2%)
		tax_percentage: float = 0.05
		# TODO: Remove coupling between specific brands of electric car
		#  and information
		# TODO: Group information by their "Domain" their type, class, behaviour
		if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
			tax_percentage = 0.02

		# Compute the payable tax
		payable_tax = tax_percentage * catalogue_price

		# Print out the vehicle registration information
		print("Registration Complete. Vehicle Information:")
		print(f"Brand: {brand}")
		print(f"Id: {vehicle.id}")
		print(f"License Plate{vehicle.license_plate}")
		print(f"Payable Tax: {payable_tax}")

app = Application()
app.register_vehicle("BMW 5")
