# You're building an inventory tool for a pharmacy.
#
# Write a tool that accepts a medication name and quantity, but assumes
# a standard quantity of 30 if none is specified.
# Order two medications — one using the default, one with a custom quantity.

def pharmacy_inventory(medication_name, quantity=30):
    """Prints the name and quantity of the medication being prescribed."""
    print(f"\nMedication: {medication_name.title()}")
    print(f"Quantity: {quantity}")

pharmacy_inventory(medication_name='advil')
pharmacy_inventory(medication_name='tylenol', quantity=60)