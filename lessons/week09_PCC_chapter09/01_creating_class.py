# Chapter 9 Part 1: Creating and Using a Class (PCC, pg. 158-161)

# A class is a blueprint for creating objects
# Class names use CamelCase by convention (capitalized, no underscores)

class Dog:
    """A simple attempt to model a dog."""

    # __init__ runs automatically every time a new instance is created
    # 'self' is a reference to the instance being created – it must come first
    # 'name' and 'age' are the values we pass in when creating a dog

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    # Methods are functions that belong to a class
    # 'self' is still required as the first parameter

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Instantiating a Dog object –– passing name and age, self is handled
# automatically

my_dog = Dog('Willie', 6)

# Dot notation access the attribute attached to this specific instance

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods on an instance using dot notation

my_dog.sit()
my_dog.roll_over()

# Each instance is independent –– they share the blueprint but not the data

your_dog = Dog('Lucy', 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# TIY

# 9-1. Restaurant: Make a class called Restaurant. The
# __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a method called
# describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that
# prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print
# the two attributes individually, and then call both methods.

class Restaurant:
    """Models restaurants."""
    def __init__(self, name, cuisine):
        """Attaches a name and cuisine to a restaurant."""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Prints the name and style of food for the restaurant."""
        print(f"\n{self.name.title()} serves {self.cuisine} food.")

    def open_restaurant(self):
        """Prints a message that the restaurant is now open."""
        print(f"{self.name.title()} is now open!")

restaurant = Restaurant('台湾小吃', 'Taiwanese')

print(f"\nRestaurant name: {restaurant.name.title()}")
print(f"Cuisine type: {restaurant.cuisine}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise
# 9-1. Create three different instances from the class, and
# call describe_restaurant() for each instance.

restaurant_0 = Restaurant('la comida bonita', 'Spanish')
restaurant_1 = Restaurant('lone star brisket', 'BBQ')
restaurant_2 = Restaurant('vesuvio', 'Italian')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

# 9-3. Users: Make a class called User. Create two attributes
# called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary
# of the user's information. Make another method called
# greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and
# call both methods for each user.

class User:
    """Used to build user profiles."""

    def __init__(self, first_name, last_name, user_name, email, phone_number):
        """Instantializes the user with requires profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
    
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

user_0 = User('john', 'smith', 'smitty44', 'j.smith@smith.ai', 1234567890)
user_1 = User('jane', 'doe', 'jane_tha_deer', 'jane_doe@doenco.com', 9876543210)

user_0.describe_user()
user_1.describe_user()

user_0.greet_user()
user_1.greet_user()