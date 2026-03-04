# You're building a lead tracking tool for a sales team.
#
# Write a tool that accepts a first and last name and returns
# a dictionary storing both values.
# Build two leads and print the returned dictionaries.

def lead_tool(first_name, last_name):
    """Builds a dictionary to store leads for sales team."""
    lead_tracker = {'first_name':first_name, 'last_name':last_name}
    return lead_tracker

lead_0 = lead_tool('john', 'smith')
print(lead_0)

lead_1 = lead_tool('jane', 'doe')
print(lead_1)