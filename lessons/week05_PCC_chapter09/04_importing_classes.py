# Chapter 9 Part 4: Importing Classes (PCC, pg. 174-179)

# import just the Car class from the car module

from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# importing multiple classes from the same module

# from car import ElectricCar # edited later on in lesson, have to omit

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# You can import multiple classes in one import statement

from car import Car #, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

# import the whole module -- access classes with module_name.ClassName

import car

my_beetle = car.Car('volkswagen', 'beetle', 2024)
print(my_beetle.get_descriptive_name())

# importing from separate modules

from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# alias a class at import to shorten long names

from electric_car import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# alias as an entire module

import electric_car as ec

my_leaf2 = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf2.get_descriptive_name())

# 9-10. Imported Restaurant: Using your latest Restaurant class,
# store it in a module. Make a separate file that imports
# Restaurant. Make a Restaurant instance, and call one of
# Restaurant's methods to show that the import statement is
# working properly.

import restaurant

new_restaurant = restaurant.Restaurant('chomp chomp chiminchanga', 'Mexican')
new_restaurant.describe_restaurant()

# 9-11. Imported Admin: Start with your work from Exercise 9-8.
# Store the classes User, Privileges, and Admin in one module.
# Create a separate file, make an Admin instance, and call
# show_privileges() to show that everything is working correctly.

# from user import Admin # Will not run after completing 9-12

# new_admin = Admin('doug', 'pugsworth', 'doug.pug', 'd-pug@pug.org', 7629492648)
# new_admin.privileges.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module,
# and store the Privileges and Admin classes in a separate
# module. In a separate file, create an Admin instance and
# call show_privileges() to show that everything is still
# working correctly.

from admin_privileges import Admin

new_admin2 = Admin('joe', 'shmoe', 'shmoester221', 'joeshmoe@shmoeco.com', 4728429247)
new_admin2.privileges.show_privileges()