# Stores classes for problem_13, 14, 15, 16

from problem_16_module import Payments

class LoanApplications:
    """Used to generate new loan applications."""
    def __init__(self, name, loan_number, payment_percentage):
        """Defines attributes of the loan."""
        self.name = name
        self.loan_number = loan_number
        self.payment_percentage = Payments(payment_percentage)
        if self.payment_percentage.payment_percent >= 0.95:
            self.interest = 0.05
        else:
            self.interest = 0.07
    
    def show_loan(self):
        """Prints the terms of the loan."""
        print(f"\nLoan Number: {self.loan_number}")
        print(f"\tBorrower: {self.name.title()}")
        print(f"\tInterest: {round(self.interest * 100, 2)}%")

class AccountManagement:
    """Hypothetical class to test importing a class."""