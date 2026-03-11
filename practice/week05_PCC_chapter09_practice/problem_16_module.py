# Module for problem_16.py

class Payments:
    """Used to track payments."""
    def __init__(self, payment_percent):
        """Instantiates the attributes for payments."""
        self.payment_percent = payment_percent
    
    def show_payments(self):
        """Prints payment percentage."""
        print(f"You have made {self.payment_percent * 100}% of payments.")