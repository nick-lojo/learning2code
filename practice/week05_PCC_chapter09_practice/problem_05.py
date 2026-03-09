# A car rental company needs to track their fleet in code.
# Every car in the fleet starts with zero miles on it.
# This value should be set automatically — the employee
# registering the car should not have to provide it.
#
# Create one car and confirm the starting mileage is correct.

class RentalCars:
    """Creates rental cars for a company's fleet."""
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.mileage = 0
    
    def confirm_mileage(self):
        """Confirms the mileage for the vehicle."""
        print(f"The {self.model.title()} has {self.mileage} miles on it.")

vehicle_0 = RentalCars('nissan', 'sentra')
vehicle_0.confirm_mileage()