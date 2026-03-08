# Chapter 9 Part 3: Inheritance (PCC, pg. 167-172)

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attriobutes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # odometer always starts at 0 – no parameter needed.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name
        
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the amount given to the odometer reading."""
        self.odometer_reading += miles

# Add battery class from pg. 170

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

# Child class inherits all attributes and methods from Car
# super() calls the parent __init__() to set up share attributes

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

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.fill_gas_tank()

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# TIY

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of
# restaurant. Write a class called IceCreamStand that inherits
# from the Restaurant class you wrote in Exercise 9-1 or 9-4.
# Either version will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream
# flavors. Write a method that displays these flavors. Create an
# instance of IceCreamStand, and call this method.

class Restaurant:
    """Models restaurants."""
    def __init__(self, name, cuisine):
        """Attaches a name and cuisine to a restaurant."""
        self.name = name
        self.cuisine = cuisine
        self.customers_served = 0
    
    def describe_restaurant(self):
        """Prints the name and style of food for the restaurant."""
        print(f"\n{self.name.title()} serves {self.cuisine}.")

    def open_restaurant(self):
        """Prints a message that the restaurant is now open."""
        print(f"{self.name.title()} is now open!")
    
    def share_served(self):
        """Shares how many customers the restaurant has served."""
        print(f"\n{self.name.title()} has served {self.customers_served} customers.")

    def set_number_served(self, served):
        """Let's you set the number of customers served."""
        if served >= self.customers_served:
            self.customers_served = served
        else:
            print("You can't un-serve a customer!")
    
    def increment_number_served(self, serves):
        """Incrementally add to the total number of customers served."""
        self.customers_served += serves

class IceCreamStand(Restaurant):
    """Models an ice cream stand, which is a sub-class of restaurants."""
    def __init__(self, name, cuisine='ice cream'):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def available_flavors(self):
        """Displays the flavors available at the stand."""
        print(f"\n{self.name.title()} serves the following flavors:")
        for flavor in self.flavors:
            print(f"\t– {flavor}")

my_stand = IceCreamStand('scoop scoop, hooray!')
my_stand.available_flavors()

# 9-7. Admin: An administrator is a special kind of user. Write a
# class called Admin that inherits from the User class you wrote
# in Exercise 9-3 or 9-5. Add an attribute, privileges, that
# stores a list of strings like "can add post", "can delete post",
# "can ban user", and so on. Write a method called
# show_privileges() that lists the administrator's set of
# privileges. Create an instance of Admin and call your method.

class User:
    """Used to build user profiles."""

    def __init__(self, first_name, last_name, user_name, email, phone_number):
        """Instantializes the user with requires profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints the user and their required information."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nName: {full_name.title()}")
        print(f"\tUsername: {self.user_name}")
        print(f"\tEmail: {self.email}")
        print(f"\tPhone Number: {self.phone_number}")
    
    def greet_user(self):
        """Prints a custom greeting for the user."""
        print(f"\nWelcome back, {self.user_name}!")

    def share_attempts(self):
        """Prints the number of log-in attempts made by the user."""
        if self.login_attempts == 1:
            print(f"\nYou have tried to log-in once.")
        else:
            print(f"\nYou have tried to log-in {self.login_attempts} times.")
    
    def increment_logins(self):
        """Increments log-in attempts one at a time."""
        self.login_attempts += 1
        self.share_attempts()
    
    def reset_login_attempts(self):
        """Resets the number of log-in attempts to 0."""
        self.login_attempts = 0
        print(f"\nYou have reset your log-in attempts.")
        self.share_attempts()

class Privileges:
    """A class specifically for Admin privileges."""
    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        """Creates the list attribute of privileges."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Shows the special privileges of Admins."""
        print(f"\nIn addition to the same privileges as users, admins have the folllowing privileges:")
        for privilege in self.privileges:
            print(f"\t– {privilege}")

class Admin(User):
    """Special class of User with special privileges."""
    def __init__(self, first_name, last_name, user_name, email, phone_number):
        """Brings over attributes from original User class and super to edit
        new ones."""
        super().__init__(first_name, last_name, user_name, email, phone_number)
        self.privileges = Privileges()

new_admin = Admin('billy', 'jenkins', 'i_am_bill_jenk', 'billy.j@jenkingsinc.com',
                  82747829463)

# 9-8. Privileges: Write a separate Privileges class. The class
# should have one attribute, privileges, that stores a list of
# strings as described in Exercise 9-7. Move the show_privileges()
# method to this class. Make a Privileges instance as an attribute
# in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

new_admin.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py
# from this section. Add a method to the Battery class called
# upgrade_battery(). This method should check the battery size
# and set the capacity to 65 if it isn't already. Make an
# electric car with a default battery size, call get_range()
# once, then call get_range() a second time after upgrading
# the battery. You should see an increase in the car's range.

ev = ElectricCar('tesla', 'm3', 2021)

ev.battery.get_range()
ev.battery.upgrade_battery()
ev.battery.get_range()