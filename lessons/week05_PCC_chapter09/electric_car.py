"""A module used to model an electric car through classes."""

from car import Car

"""A class that can be used as an attribute in the ElectricCar sub-class"""

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        # default value means battery_size is optional at instantiation
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrades battery to 65 kWh if not already."""
        if self.battery_size == 65:
            print("This car's battery is already upgraded.")
        elif self.battery_size == 40:
            self.battery_size = 65
            print(f"We have upgraded your battery to {self.battery_size}-kWh.")

"""A sub-class that can be used to model an electric car."""

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specifc to an electric car."""
        super().__init__(make, model, year)
        # battery_size is specifc to ElectricCar, not Car
        # self.battery_size = 40 # Don't need this now that we are using Battery()
        # Battery is its own class -- assigned as an attribute of ElectricCar
        self.battery = Battery()
    
    # def describe_battery(self): # don't need this now that it is in Battery()
    #     """Print a statement describe the battery size."""
    #     print(f"This car has a {self.battery}-kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")