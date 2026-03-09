"""A module that can be used to model user profiles."""

class User:
    """Used to build user profiles."""

    def __init__(self, first_name, last_name, user_name, email, phone_number):
        """Instantializes the user with requires profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints the user and their required information."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nName: {full_name.title()}")
        print(f"\tUsername: {self.user_name}")
        print(f"\tEmail: {self.email}")
        print(f"\tPhone Number: {self.phone_number}")
    
    def greet_user(self):
        """Prints a custom greeting for the user."""
        print(f"\nWelcome back, {self.user_name}!")

    def share_attempts(self):
        """Prints the number of log-in attempts made by the user."""
        if self.login_attempts == 1:
            print(f"\nYou have tried to log-in once.")
        else:
            print(f"\nYou have tried to log-in {self.login_attempts} times.")
    
    def increment_logins(self):
        """Increments log-in attempts one at a time."""
        self.login_attempts += 1
        self.share_attempts()
    
    def reset_login_attempts(self):
        """Resets the number of log-in attempts to 0."""
        self.login_attempts = 0
        print(f"\nYou have reset your log-in attempts.")
        self.share_attempts()