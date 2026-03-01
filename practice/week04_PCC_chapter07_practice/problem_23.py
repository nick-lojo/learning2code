# You're writing a dispatch tool for a courier company.
#
# A manager needs to process a list of pending deliveries and move them
# to a completed list one at a time.
# Print a message as each delivery is processed.
# After all deliveries are processed, print the completed list.
#
# Pending: ['downtown', 'airport', 'suburbs', 'harbor']

pending = ['downtown', 'airport', 'suburbs', 'harbor']
completed = []

while pending:
    processed = pending.pop()
    print(f"Delivery to {processed} is processed.")
    completed.append(processed)

print('\nCompleted Deliveries:')
for delivery in completed:
    print(f"\t{delivery.title()}")