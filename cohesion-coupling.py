"""
Dev Notes: Practice of Software Quality Metrics related concepts
    - Cohesion
    - Coupling
"""

import string
import random


class VehicleRegistry:
	def generate_vehicle_id(self, lenght) -> str:
        	return ''.join(random.choices(string.ascii_uppercase, k=lenght))

	def generate_vehicle_license(self, id) -> str:
        	return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
	def register_vehicle(self, brand: str) -> None:
		# Creates a registry instance
		registry: VehicleRegistry = VehicleRegistry()
		
		# Creates a vehicle id of lenght 12
		vehicle_id: str = registry.generate_vehicle_id(12)

		# Creates a license plate for the vehicle
		# using the frist two characters of the vehicle id
		license_plate: str = registry.generate_vehicle_license(vehicle_id)

		# Computes the catalogue price
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
		if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
			tax_percentage = 0.02

		# Compute the payable tax
		payable_tax = tax_percentage * catalogue_price

		# Print out the vehicle registration information
		print("Registration Complete. Vehicle Information:")
		print(f"Brand: {brand}")
		print(f"Id: {vehicle_id}")
		print(f"License Plate{license_plate}")
		print(f"Payable Tax: {payable_tax}")

app = Application()
app.register_vehicle("BMW 5")
