# Chapter 9 Part 2: Working with Classes and Instances (PCC, pg. 162-166)

# Attributes can be given default values directly in __init__()
# without being passed in as parameters

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

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# You can change an attribute's value directly through the instance

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# updating through a method lets you add logic/validation

my_new_car.update_odometer(50)
my_new_car.read_odometer()

# try to roll it back -- should trigger the else

my_new_car.update_odometer(10)

# increment is useful when you know how many miles were added rather
# than what the total should be

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# TIY

# 9-4. Number Served: Start with your program from Exercise 9-1.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the
# number of customers the restaurant has served, then change this
# value and print it again.
# Add a method called set_number_served() that lets you set the
# number of customers that have been served. Call this method with
# a new number and print the value again.
# Add a method called increment_number_served() that lets you
# increment the number of customers who've been served. Call this
# method with any number that could represent how many customers
# were served in a day of business.

class Restaurant:
    """Models restaurants."""
    def __init__(self, name, cuisine):
        """Attaches a name and cuisine to a restaurant."""
        self.name = name
        self.cuisine = cuisine
        self.customers_served = 0
    
    def describe_restaurant(self):
        """Prints the name and style of food for the restaurant."""
        print(f"\n{self.name.title()} serves {self.cuisine} food.")

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

new_restaurant = Restaurant('big boy grill', 'american')

new_restaurant.share_served()

new_restaurant.set_number_served(6)
new_restaurant.share_served()

new_restaurant.set_number_served(5)

new_restaurant.increment_number_served(13)
new_restaurant.share_served()

# 9-5. Login Attempts: Add an attribute called login_attempts to
# your User class from Exercise 9-3. Write a method called
# increment_login_attempts() that increments login_attempts by 1.
# Write another method called reset_login_attempts() that resets
# login_attempts to 0.
# Make an instance of User and call increment_login_attempts()
# several times. Print login_attempts to make sure it incremented
# properly, then call reset_login_attempts(). Print login_attempts
# again to make sure it was reset to 0.

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

new_user = User('jessi', 'jones', 'jj19', 'j_jonez19@jonescorp.net', 3920938531)

new_user.share_attempts()

new_user.increment_logins()
new_user.increment_logins()
new_user.increment_logins()
new_user.increment_logins()
new_user.increment_logins()
new_user.increment_logins()

new_user.reset_login_attempts()