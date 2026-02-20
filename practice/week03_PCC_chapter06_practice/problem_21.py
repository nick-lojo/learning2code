# You're managing a contact list with detailed information.
#
# Create a dictionary called contacts.
#
# Inside contacts, create two entries:
# - 'mom': a dictionary with phone='555-0100', email='mom@email.com'
# - 'boss': a dictionary with phone='555-0200', email='boss@work.com'
#
# Loop through the contacts dictionary.
# For each contact, print their name and phone number.

contacts = {
    'mom':{
        'phone':'555-0100',
        'email':'mom@email.com'
    },
    'boss':{
        'phone':'555-0200',
        'email':'boss@work.com'
    }
}

for name, contact_info in contacts.items():
    print(f"\nName: {name.title()}")
    print(f"\tPhone: {contact_info['phone']}")