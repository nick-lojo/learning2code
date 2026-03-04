# You're building a shipping label tool for an e-commerce company.
#
# Write a tool that accepts a recipient's name and city.
# Call it using the recipient's name and city explicitly labeled.

def label_maker(name, city):
    """Accept's the recipients name and city for a shipping label."""
    print(f"Shipping to {name.title()} in {city.title()}.")

label_maker(city='seattle', name='sam')