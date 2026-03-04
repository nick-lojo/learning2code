# You're building a name formatting tool for a law firm's case management system.
#
# Write a tool that accepts a first and last name and sends back
# a properly formatted full name.
# Format two attorney names and print the results.

def format_case_manager(first_name, last_name):
    """Formats the full name of the attorney assigned to a case."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

lawyer_0 = format_case_manager('john', 'doe')
print(lawyer_0)

lawyer_1 = format_case_manager('jane', 'smith')
print(lawyer_1)