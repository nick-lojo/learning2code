# A public library tracks how many times a book has been checked out.
# A librarian needs to correct the checkout count for a book
# that was miscounted during a system migration.
#
# Create one book and correct the count directly.
# Print the value before and after.

class Book:
    """A class used for libraries to track their inventory."""
    def __init__(self, title, author, checked_out):
        """Set up attributes of the class."""
        self.title = title
        self.author = author
        self.checked_out = checked_out
    
    def times_check_out(self):
        """Prints the number of times a book was checked out."""
        print(f"This book has been checked out {self.checked_out} times.")

book_0 = Book('hunger games', 'suzanne collins', 2)
book_0.times_check_out()
book_0.checked_out = 44
book_0.times_check_out()