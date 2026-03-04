# You're building an onboarding tool for a property management company.
#
# Write a tool that always accepts a tenant's first and last name,
# plus any number of labeled details about their lease.
# Onboard one tenant with at least three lease details and print the result.

def tenant_management(first_name, last_name, **lease_details):
    """Always a property manager to store information about their tenants
    and their leases."""
    lease_details['first name'] = first_name.title()
    lease_details['last name'] = last_name.title()
    return lease_details

tenant_0 = tenant_management('jane', 'doe',
                             monthly_rent=2500,
                             unit_number='36B',
                             number_bedrooms='2')

print(tenant_0)