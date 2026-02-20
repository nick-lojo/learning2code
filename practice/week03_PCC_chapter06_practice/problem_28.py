# You're analyzing customer feedback ratings.
#
# Create a dictionary of customers and their satisfaction ratings:
# - 'Customer_A': 4
# - 'Customer_B': 5
# - 'Customer_C': 3
# - 'Customer_D': 5
# - 'Customer_E': 4
#
# Print all unique rating values that were given (no duplicates).

satisfaction_ratings = {
    'Customer A':4,
    'Customer B':5,
    'Customer C':3,
    'Customer D':5,
    'Customer E':4
}

print('Unique Rating Values:')
for rating in set(satisfaction_ratings.values()):
    print(f"{rating}")