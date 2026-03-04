# TIY Import Statement

import printing_functions

# Chapter 8 Part 6: Modules (PCC, pg. 149-154)

# Importing an entire module makes all its functions available
# Use dot notation to call functions: module_name.function_name()

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# You can import just the function you need from a module
# No dot notation required – call the function directly by name

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# An alias gives a function or module a shorter name using the 'as' keyword
# Useful when a name is long or conflicts with something else in your program

# Alias for a function
from pizza import make_pizza as mp
mp(16, 'pepperoni')

# Alias for a module
import pizza as p
p.make_pizza(12, "mushrooms", 'green peppers', 'extra cheese')

# The asterisk imports every function from the module into your program
# You can call functions directly without dot notation
# Avoid this with large modules – naming conflicts can silently overwrite functions

from pizza import *
make_pizza(16, 'pepperoni')

# Styling Functions

# Function and module names use lowercase letters and underscores
# Every function should have a docstring immediately after the def line
# No spaces around = siggns in default values or keyword arguments
# Limit lines to 79 characters – break long parameter lists with indentation
# Separate multiple functions with two blank lines
# All import statements go at the top of the file

# TIY

# 8-15. Printing Models: Put the print_models() and show_completed_models()
# functions into a separate file called printing_functions.py. Write an import
# statement at the top of your modules.py file and call both functions using
# the imported module.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8-16. Imports: Using a program you wrote that has one function in it, store
# that function in a separate file. Import the function into your main program
# file using each of these approaches:
# import module_name

import function_file

usernames = ['hannah', 'ty', 'margot']
function_file.greet_users(usernames)

# from module_name import function_name

from function_file import greet_users

usernames = ['hannah', 'ty', 'margot']
function_file.greet_users(usernames)

# from module_name import function_name as fn

from function_file import greet_users as gu

usernames = ['hannah', 'ty', 'margot']
gu(usernames)

# import module_name as mn

import function_file as ff

usernames = ['hannah', 'ty', 'margot']
ff.greet_users(usernames)

# from module_name import *

from function_file import *

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)