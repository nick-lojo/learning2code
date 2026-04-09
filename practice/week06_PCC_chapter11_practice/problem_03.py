# You wrote a function called format_policy_number() that takes
# a carrier prefix and a numeric ID, and returns a formatted
# string like "HIO-00482".
#
# A colleague asks: "How do we know it actually works?"
# You decide to write an automated test instead of running
# the program manually each time.
#
# In this file:
# 1. Write the function format_policy_number() in a file
#    called policy_functions.py
# 2. Write a test file called test_policy_functions.py
#    with one test that verifies the function returns the
#    correct formatted string for a known input.

def format_policy_number(carrier_prefix, numeric_id):
    """Returns the policy number as a formatted string."""
    policy_number = f"{carrier_prefix}-{numeric_id}"
    print(f'Policy Number: {policy_number.upper()}')
    return policy_number.upper()