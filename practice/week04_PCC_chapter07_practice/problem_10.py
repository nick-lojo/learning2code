# You're writing a safety check for a script before it goes to production.
#
# Review this code and identify why it will never stop running.
# Fix it so the loop terminates correctly after printing numbers 1 through 5.

# x = 1
# while x <= 5:
#    print(x)

# This code will never stop because we are not changing the value of x.
# As written, x will always equal 1. We need to add a line to change the value
# of x.

# Correct Solution

x = 1
while x <= 5:
    print(x)
    x = x + 1