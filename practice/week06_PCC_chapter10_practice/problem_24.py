# A hotel booking system calculates the cost per night for a stay.
# It divides the total bill by the number of nights.
# If the calculation fails, print a friendly message.
# If it succeeds, print the result — but only if it succeeded.
#
# Your job: prompt the user for total bill and number of nights.
# Calculate and display the nightly rate.

def nightly_cost():
    """Helps customers calculate the cost per night at a hotel."""
    print("\nLet's calculate your cost per night!")
    print("Please enter your total bill, and number of nights when prompted.")

    total_cost = input("\nWhat was the total cost of your stay? ")
    total_nights = input("How many nights did you stay? ")

    try:
        average_cost = int(total_cost) / int(total_nights)
    except ZeroDivisionError:
        print("\nThe number of nights you stayed must be greater than zero.")
    else:
        print(f"\nYour average cost per night is: ${average_cost}")

nightly_cost()