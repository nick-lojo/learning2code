# A logistics company needs to track their delivery vehicles in code.
# Each vehicle has a make and a year.
#
# Build this so every new vehicle is created with those two pieces of information.
# Create one vehicle and print both values.

class DeliveryVehicles:
    """A simple code to build delivery vehicles."""
    def __init__(self, make, year):
        self.make = make
        self.year = year
    
vehicle_0 = DeliveryVehicles('mercedes', 2021)
print(f"Our delivery fleet includes a {vehicle_0.year} {vehicle_0.make.title()}.")