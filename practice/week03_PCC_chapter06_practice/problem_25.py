# You're organizing a library checkout system.
#
# Create a dictionary with three books and who checked them out:
# - 'Python Basics': 'Alice'
# - '1984': 'Bob'
# - 'Dune': 'Charlie'
#
# Alice returns 'Python Basics' (remove it from the dictionary).
# Someone new checks out 'Neuromancer' - add Dave as the borrower.
#
# Print all currently checked out books and their borrowers.

library_checkout = {
    'Python Basics':'Alice',
    '1984':'Bob',
    'Dune':'Charlie'
}

del library_checkout['Python Basics']

library_checkout['Neuromancer'] = 'Dave'

print('Books Currently Checked Out')

for book, borrower in library_checkout.items():
    print(f"\nBook: {book}")
    print(f"\tBorrower: {borrower}")