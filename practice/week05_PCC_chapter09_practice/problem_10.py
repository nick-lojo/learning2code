# A logistics company has a general vehicle in their system.
# Refrigerated trucks are a specific kind of vehicle that
# have their own attributes and behaviors general vehicles don't have.
#
# Build the refrigerated truck as an extension of the general vehicle.
# Give it at least one unique attribute and one unique method.
# Create one instance and demonstrate both.

class GeneralVehicle:
    """Builds a class for general vehicles."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_details(self):
        """Provides the details of a vehicle."""
        vehicle_details = f"{self.year} {self.make.title()} {self.model.title()}"
        return vehicle_details

class RefrigeratedTruck(GeneralVehicle):
    """A sub-class of vehicles that can transport refridgerated goods."""
    def __init__(self, make, model, year, fridge_temp):
        """Define existing attributes, and new ones."""
        super().__init__(make, model, year)
        self.fridge_temp = fridge_temp

    def update_fridge_temp(self, new_temp):
        """Can be used to change the temperature of a fridge."""
        self.fridge_temp = new_temp
        print(f"The temperature has been updated to {self.fridge_temp} degrees.")

truck_0 = RefrigeratedTruck('subaru', 'sambar', 1995, 32)
print(truck_0.get_details())
truck_0.update_fridge_temp(20)