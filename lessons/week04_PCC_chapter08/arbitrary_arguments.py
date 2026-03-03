# Chapter 8 Part 5: Arbitrary Arguments (PCC, pg. 146-149)

# *toppings tells Python to collect all remaining arguments into a tuple
# Use this when you don't know ahead of time how many arguments will be passed

def make_pizza(*toppings):
    """Summarizing the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"– {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# When mixing positional and arbitrary arguments, positional comes first
# Python assigns the first argument to size, then packs the rest into toppins

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"– {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')\

# **user_info tells Python to collect all extra keyword arguments into a dictionary
# Use this when you don't know what kind of information will be passed

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# TIY

# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich using *args. Print a summary of the sandwich being
# ordered. Call the function three times with a different number of arguments.

def make_sandwich(*toppings):
    """Prints the toppings being added to a sandwich."""
    print("\nAdding the following toppings to your sandwich:")
    for topping in toppings:
        print(f"– {topping}")

make_sandwich('chicken cutlet')
make_sandwich('turkey', 'provolone cheese')
make_sandwich('bacon', 'lettuce', 'tomato')

# 8-13. User Profile: Build a profile of yourself by calling build_profile()
# using your first and last name and three other key-value pairs.

def build_profile(first, last, **user_details):
    """Stores the user's profile details in a dictionary."""
    user_details['first_name'] = first
    user_details['last_name'] = last
    return user_details

user_profile = build_profile('drake', 'maye',
                             position='QB',
                             team='patriots')

print(user_profile)

# 8-14. Cars: Write a function called make_car() that always receives a
# manufacturer and model name, then accepts an arbitrary number of keyword
# arguments. Call it with the required info and two other name-value pairs.
# Print the dictionary returned to confirm everything stored correctly.

def make_car(manufacturer, model_name, **car_info):
    """Stores details about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name
    return car_info

car = make_car('mclaren', 'p1',
               color='orange',
               cost=1250000)

print(car)