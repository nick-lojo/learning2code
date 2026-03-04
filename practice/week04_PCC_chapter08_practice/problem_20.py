# You're building a client intake tool for a law firm.
#
# Write a tool that always accepts a client's first and last name,
# plus any number of additional labeled details about the case.
# Build one client record and print the result.

def client_intake(first_name, last_name, **case_details):
    case_details['first name'] = first_name.title()
    case_details['last name'] = last_name.title()
    return case_details

case_0 = client_intake('john', 'smith',
                       case_type='civil',
                       notes='suing neighor for property damage caused by' \
                       ' fallen tree')

print(case_0)