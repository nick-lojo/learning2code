# Chapter 8 Part 1: Defining Functions (PCC, pg. 129-131)

# A function is a named block of code you define once and reuse anywhere
# def tells Python you're creating a function
# The body is indented, and you run it by calling its name with parentheses

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# A function can accept information through a parameter
# username is a placeholder – it takes whatever value you pass in the call

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# A parameter is the variable listed in the function definition
# An argument is the actual value passed in the function call
# In greet_user('jesse') – user name is the parameter, 'jesse' is the argument

#TIY

# 8-1. Message: Write a function called display_message() that prints one
# sentence telling everyone what you are learning about in this chapter.
# Call the function and make sure the message displays correctly.

def display_message():
    """This function shares what I am learning about this chapter."""
    print("PCC Chapter 8 has taught me how to define functions, and" \
    " pass information to them using parameters and arguments.")

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts
# one parameter, title. The function should print a message such as
# "One of my favorite books is Alice in Wonderland." Call the function,
# making sure to include a book title as an argument in the function call.

def favorite_book(book):
    """Prints a message about the user's favorite book."""
    print(f"One of my favorite books is {book.title()}.")

favorite_book('harry potter')