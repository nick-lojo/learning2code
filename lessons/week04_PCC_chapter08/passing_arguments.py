# Chapter 8 Part 2: Passing Arguments (PCC, pg. 132-136)

# Positional arguments must be passed in the same order as the parameters
# Python matches each argument to a parameter based on position

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Order matters with positional arguments - swap them and you get the wrong
# output
# Python has no way to know you mixed them up

describe_pet('harry', 'hamster')

# You can call a function as many times as needed
# Each call is independent – Python runs the full function body each time

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments explicityly name which parameter gets which value
# Order no longer matters because Python knows where each value goes

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

# A default value is used when no argument is provided for that parameter
# Parameters with defaults must come after parameters without defaults

def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='harry',animal_type='hamster')

# Equivalent Function Calls
# Multiple calling styles work for the same function – use whatever is clearest
# These all produce identical output for describe_pet()

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type="hamster")
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Errors
# Calling a function with too few or too many arguments raises a TypeError
# Python's error message names the missing arguments – read tracebacks carefully

#TIY

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt. The function
# should print a sentence summarizing the size of the shirt and the message.
# Call the function once using positional arguments and once using keyword
# arguments.

def make_shirt(size, message):
    """Summarizes size of the shirt and the message to be printed."""
    print(f'\nThe shirt is a size {size.upper()} with the message "{message}".')

# Positional
make_shirt('m', 'I <3 Drake Maye')

# Keyword
make_shirt(message="I <3 Drake Maye", size='large')

# 8-4. Large Shirts: Modify make_shirt() so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a medium
# shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size='large', message='I love Python'):
    """Makes a shirt with default message and default size."""
    print(f'\nThe shirt is a size {size.upper()} with the message "{message}".')

make_shirt()
make_shirt(size='medium')
make_shirt(message='I <3 Drake Maye',size='xl')

# 8-5. Cities: Write a function called describe_city() that accepts the name
# of a city and its country. Print a simple sentence such as
# "Reykjavik is in Iceland." Give the country parameter a default value.
# Call your function for three different cities, at least one of which is
# not in the default country.

def describe_city(city, country='Spain'):
    """States the name of a city and the country it is in."""
    print(f"\n{city.title()} is in {country.title()}")

describe_city('madrid')
describe_city('a coruna')
describe_city('valencia')
describe_city('otaru', 'japan')