# You're building a fraud detection tool for a credit card company.
#
# A list of transactions needs to be scanned.
# Write a tool that accepts the list and flags each transaction as reviewed.
# Print a confirmation for each one.

def scan_transcations(pending_transactions, reviewed_transactions):
    while pending_transactions:
        processing = pending_transactions.pop(0)
        print(f"Processing {processing}...")
        reviewed_transactions.append(processing)

def completed_transactions(reviewed_transactions):
    print(f"\nThe following transactions have been reviewed for fraud:")
    for transaction in reviewed_transactions:
        print(f"\t{transaction}")

pending = ['transaction_0', 'transaction_1', 'transaction_2']
reviewed = []

scan_transcations(pending, reviewed)
completed_transactions(reviewed)