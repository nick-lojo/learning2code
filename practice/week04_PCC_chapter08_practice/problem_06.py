# You're building a payroll tool for a staffing agency.
#
# Write a tool that accepts an employee's first and last name,
# then returns their full name formatted for a pay stub.
# Print the result for two employees.

def payroll_tool(first_name, last_name):
    """Tool for payroll that formats an employees first and last name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

employee_0 = payroll_tool('john', 'smith')
print(employee_0)

employee_1 = payroll_tool('jane', 'doe')
print(employee_1)