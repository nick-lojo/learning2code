def paystub_tool(first_name, last_name, salary):
    """Formats employee paystubs."""
    full_name = f"{first_name} {last_name}"
    paystub = f"\nEmployee Name: {full_name.title()}"
    paystub += f"\nAnnual Salary: ${salary}"
    paystub += f"\n\tPaycheck: ${salary / 26}"
    return paystub