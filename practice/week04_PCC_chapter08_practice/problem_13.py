# You're building a user profile tool for a fitness app.
#
# Write a tool that accepts a user's first and last name, plus any
# number of additional details about them.
# Build one profile with extra details and print the result.

def user_profile(first_name, last_name, *additional_details):
    """Builds profiles for users of a fitness app."""
    full_name = f"{first_name} {last_name}"
    profile = f"\nName: {full_name}\nOther Details:\n\t{additional_details}"
    return profile

user_0 = user_profile('john', 'doe', 2125550000, '123 Main St')
print(user_0)