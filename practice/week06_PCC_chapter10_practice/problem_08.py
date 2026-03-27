# A pit crew tool calculates a driver's average lap time.
# It divides total race time by number of laps completed.
# If the calculation succeeds, the result should print.
# If it fails, print a friendly message.
#
# The result should only print if the calculation actually
# succeeded — keep success and failure logic separate.

print("\nI can calculate the average lap time.")
print("Enter your total race time and laps completed.")

total_time = input(f"\nWhat is the total race time (in minutes)? ")
total_laps = input(f"How many total laps have you raced? ")

try:
    average_lap = int(total_time) / int(total_laps)
except ValueError:
    print("Please enter an integer.")
else:
    print(f"Your average lap time is {average_lap} minutes.")