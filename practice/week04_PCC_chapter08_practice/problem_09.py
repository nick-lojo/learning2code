# You're building a name lookup tool for a hospital patient portal.
#
# Write a tool that keeps asking for a patient's first and last name
# and prints a formatted greeting until the receptionist is done.
# The receptionist should be able to quit at any prompt.

def name_lookup():
    """Looks up patient's name until ended by receptionist."""
    while True:
        print("\nPlease provide the patient's first, then last, name.")
        print("Enter 'q' at any time to stop.")
        f_name = input("\nEnter the patient's first name: ")
        if f_name == 'q':
            break
        l_name = input("Please enter the patient's last name: ")
        if l_name == 'q':
            break
        full_name = f"{f_name} {l_name}"
        print(f"{full_name.title()} is ready for triage.")

name_lookup()