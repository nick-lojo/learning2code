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