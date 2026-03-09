"""A module that stores the class to model an Admin, and the class used for the privileges attribute."""

from user import User

class Privileges:
    """A class specifically for Admin privileges."""
    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        """Creates the list attribute of privileges."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Shows the special privileges of Admins."""
        print(f"\nIn addition to the same privileges as users, admins have the folllowing privileges:")
        for privilege in self.privileges:
            print(f"\t– {privilege}")

class Admin(User):
    """Special class of User with special privileges."""
    def __init__(self, first_name, last_name, user_name, email, phone_number):
        """Brings over attributes from original User class and super to edit
        new ones."""
        super().__init__(first_name, last_name, user_name, email, phone_number)
        self.privileges = Privileges()