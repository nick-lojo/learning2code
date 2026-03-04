# You're building a business card generator for a consulting firm.
#
# Write a tool that accepts a first name, last name, and optionally
# a job title. Return the formatted card details.
# Generate one card with a title and one without.

def business_card(first_name, last_name, job_title=''):
    """Formats business cards for a consulting firm."""
    if job_title:
        business_card = f"Name: {first_name.title()} {last_name.title()}"
        business_card += f"\nJob Title: {job_title.title()}"
    else:
        business_card = f"Name: {first_name.title()} {last_name.title()}"
    return business_card

employee_0 = business_card('jane', 'doe', job_title='president')
print(employee_0)

employee_1 = business_card('john', 'smith')
print(f"\n{employee_1}")