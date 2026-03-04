# You're building a contact card tool for a real estate CRM.
#
# Write a tool that accepts a first and last name, and optionally
# a phone number. Return the contact's information.
# Create one contact with a phone number and one without.

def contact_card(first_name, last_name, phone=None):
    """Creates contacts for real estate CRM."""
    if phone:
        full_name = f"{first_name} {last_name}"
        contact = f"Name: {full_name.title()}, Phone Number: {phone}"
    else:
        full_name = f"{first_name} {last_name}"
        contact = f"Name: {full_name.title()}"
    return contact

contact_0 = contact_card('john', 'doe', 2125550000)
print(contact_0)

contact_1 = contact_card('jane', 'doe')
print(contact_1)