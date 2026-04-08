# Chapter 11 Part 1: Testing Functions (PCC, pg. 210-217)

# pip is Python's package installer – used to install third-party libraries
# upgrade pip before installing anything new to avoid security issues
# command to run in terminal (not Python): python -m pip install --upgrade pip

# terminal output confirm: pip upgraded from 25.2 to 26.0.1
# use pythoin3 on Mac, not python – 'python' command not found on this system

# pytest is a third-party testing library – not included with Python by default
# --user flag installs it for the current user only
# command to run in terminal: python3 -m pip install --user pytest

# pytest installed to a directory not on system PATH
# fix: run with python3 -m pytest instead of just pytest
# same pattern as python3 -m pip

# before writing tests, you need a function to test
# get formatted_name() takes a first and last name,
#   combines them with a space, and returns the full
#   name in title case

# get_formatted_name() notes will stay in 01_testing_functions.py
# test_name_function.py will get its own module for the TIY

def get_formatted_name(first, last):
    """Combine first and last name with a space between them."""
    full_name = f"{first} {last}"
    return full_name.title()

# manual testing: a loop that lets users type names and check output
# works but requires human eyes every time the function changes

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

# Unit Tests and Test Cases (pg. 212)
# unit test: verifies ONE specific aspect of a function's behavior
# test case: a collection of unit test that together prove a function
#   behaves correctly across the full range of expected situations
# full coverage: unit tests covering every possible way to use a function
#   – often not realistic, focus on critical behaviors first

# A Passing Test (PCC, pg. 212-213)
# test file must start withy test_ so pytest can discover it
# test function must start with test_ for the same reason
# assert: checks that a condition is True - if False, the test fails
# call the function with known input, assert the reutrn value matches
#   what you expect

# def test_first_laste_name(): # Commented out, this actually runs in
#                              # test_namefunction.py
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# Running a Test (PCC, pg. 213-214)

# dot after filename = one test passed
# [110%] = all collected tests have been run
# "1 passed" = final confirmation, includes time taken
# pytest discovers test files by looking for files starting with test_

# A Failing Test (PCC, pg. 214-215)

# if you change a function in a way that breaks existing behavior,
#   pytest catches it fundamentally
# F in output = test failed
# FAILURES section shows exactly which test failed and why
# angle bracket > points to the line that caused the failure
# E shows the actual error - read this first when debugging
# don't change the test to make it pass - fix the code instead

# Responding to a Failed Test (PCC, pg.215-216)

# When a test fails, don't change the test - fix the code
# Changing the test to force a pass breaks the whole point of testing
# Make middle an optional parameter with a default value of ''
# Use an if block to build the full name differently depending on
#   whether a middle name was provided

# def get_formatted_name(first, last, middle=''):  # Commented out so script
#                                                  # runs. Code lives in
#                                                  # name_function.py
#     """Generate a neatly formatted full name."""
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()

# Adding New Tests (PCC, pg. 216-217)

# You can add multiple test functions to the same test file
# Each function tests ONE specific behavior
# Two dotes in output = two tests passed
# Naming test functions clearly tells you exactly what broke
#   when a test fails

# Code is commented out so script runs. Code lives in test_name_function.py

# def test_first_last_middle_name():
#     """Do names like 'Wolfgang Amadeus Mozart' work?"""
#     formatted_name = get_formatted_name(
#         'wolfgang', 'mozart', 'amadeus')
#     assert formatted_name == 'Wolfgang Amadeus Mozart'

# Two dots in output = two tests passed
# Each test function tests ONE specific behavior of the function

# TRY IT YOURSELF

# 11-1. City, Country: Write a function that accepts two parameters:
# a city name and a country name. The function should return a single
# string of the form City, Country, such as Santiago, Chile. Store
# the function in a module called city_functions.py, and save this
# file in a new folder so pytest won't try to run the tests we've
# already written.
# Create a file called test_cities.py that tests the function you
# just wrote. Write a function called test_city_country() to verify
# that calling your function with values such as 'santiago' and
# 'chile' results in the correct string. Run the test, and make sure
# test_city_country() passes.

# See files in 'tiy_functions' folder

# 11-2. Population: Modify your function so it requires a third
# parameter, population. It should now return a single string of the
# form City, Country – population xxx, such as Santiago, Chile –
# population 5000000. Run the test again, and make sure
# test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run
# the test, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that
# verifies you can call your function with the values 'santiago',
# 'chile', and population=5000000. Run the tests one more time, and
# make sure this new test passes.

# See files in 'tiy_functions' folder