# You're building a removal tool for a logistics company's shipment queue.
#
# A shipment type called 'damaged' was incorrectly added to the queue
# multiple times.
# Remove every instance of it from the list.
# Print the cleaned queue when done.
#
# Queue: ['fragile', 'damaged', 'standard', 'damaged', 'express', 'damaged']

queue = ['fragile', 'damaged', 'standard', 'damaged', 'express', 'damaged']

while 'damaged' in queue:
    queue.remove('damaged')

for item in queue:
    print(item)