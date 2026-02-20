# MINI-PROJECT: Insurance Risk Registry
# Build a commercial risk registry for a small insurance brokerage.
#
# Store 4 client accounts. Each client has: company name, industry,
# annual premium (int), coverage type, and a list of active risk flags.
# At least one client has no risk flags.
#
# Program must produce 5 outputs:
# 1. Formatted profile for each client (all details)
# 2. "High Risk Clients" section - only clients with 2+ risk flags (name +
#     premium)
# 3. Total premium volume across all clients
# 4. Each unique risk flag across all clients (no duplicates)
#
# Success criteria:
# - Runs cleanly with no errors
# - Unique risk flags contain no repeats
# - Ch. 1-6 concepts only

# CLIENT DATA:
# 1. Hargrove Logistics | Transportation | $142,000 | Commercial General
#    Liability
#    Risk flags: flood zone, poor loss history, high employee turnover
#
# 2. Meridian Capital Group | Financial Services | $98,500 | Professional
#    Liability
#    Risk flags: regulatory investigation, poor loss history
#
# 3. Bluestone Fabrication | Manufacturing | $210,000 | Commercial Property
#    Risk flags: flood zone, hazardous materials
#
# 4. Crestview Dental Partners | Healthcare | $54,000 | Professional Liability
#    Risk flags: none

client_accounts = {
    'Hargrove Logistics':{
        'industry':'Transportation',
        'annual_premium':142000,
        'coverage_type':'CGL',
        'risk_flags':['flood zone', 'poor loss history', 'high employee turnover']
    },
    'Meridian Capital Group':{
        'industry':'Financial Services',
        'annual_premium':98500,
        'coverage_type':'Professional Liability',
        'risk_flags':['regulatory investigation', 'poor loss history']
    },
    'Bluestone Fabrication':{
        'industry':'Manufacturing',
        'annual_premium':210000,
        'coverage_type':'CP',
        'risk_flags':['flood zone', 'hazardous materials']
    },
    'Crestview Dental Partners':{
        'industry':'Healthcare',
        'annual_premium':54000,
        'coverage_type':'Professional Liability'
    }
}

print('Portfolio Profile:')
for client_name, account_details in client_accounts.items():
    print(f"\nClient Name: {client_name}")
    print(f"\tAnnual Premium: ${account_details['annual_premium']}")
    print(f"\tCoverage Type: {account_details['coverage_type']}")
    no_risks = account_details.get('risk_flags', 'There are no risk flags for this account')
    print(f"\tRisk Flags:")
    print(f"\t\t{no_risks}")

print('\nHigh Risk Clients')
for client_name, account_details in client_accounts.items():
    if len(account_details.get('risk_flags', [])) > 2:
        print(f"\t{client_name} is a high risk client")

print('\nTotal Premium Volume')
total_premium = 0
for account_details in client_accounts.values():
    total_premium = total_premium + account_details['annual_premium']
print(f"\t${total_premium}")

print('\nUnique Risk Flags')
all_flags = []
for account_details in client_accounts.values():
    all_flags = all_flags + account_details.get('risk_flags', [])
for flag in set(all_flags):
    print(f"\t{flag.title()}")