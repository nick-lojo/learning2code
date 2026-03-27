# A data pipeline occasionally receives bad inputs that cause
# it to crash. You need to protect a specific calculation from
# crashing the program when something goes wrong.
#
# Your job: write a program that asks the user for two numbers
# and divides the first by the second. If something goes wrong
# during the division, print a friendly message instead of
# crashing.

print(f"Give me two numbers, and I will divide them for you!")

first_number = input("\nEnter your first number: ")
second_number = input("Enter your second number: ")

try:
    answer = int(first_number) / int(second_number)
except:
    ValueError
    print("\nYou cannot divide by 0!")
else:
    print(f"\n{answer}")