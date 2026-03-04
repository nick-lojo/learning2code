# You're building a support ticket tool for a SaaS company.
#
# Write a tool that accepts a customer name and issue description,
# then returns a formatted ticket.
# Run it for multiple customers in a single session.

def support_tool(customer_name, issue_description):
    """Formats support tickets."""
    ticket = f'\nName: {customer_name.title()}'
    ticket += f'\nIssue Description: "{issue_description}"'
    return ticket

while True:
    print("\nPlease enter your full name, and briefly describe your issue.")
    print("When you are done, eneter 'q' to stop.")

    c_name = input("\nPlease enter your full name: ")
    if c_name == 'q':
        break

    issue = input("\nPlease describe the issue you are having: ")
    if issue == 'q':
        break
    
    customer_ticket = support_tool(c_name, issue)
    print(customer_ticket)