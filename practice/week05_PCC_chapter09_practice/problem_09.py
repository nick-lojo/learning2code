# A regional bank has standard checking accounts.
# They're launching a new premium account type that works
# like a standard account but has additional features specific to premium customers.
#
# Build the premium account as an extension of the standard one.
# Create one premium account instance and confirm it has access
# to the standard account's behavior.

class CheckingAccounts:
    """Creates checking accounts for a bank."""
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
    
    def show_account(self):
        print(f"\nName: {self.name.title()}")
        print(f"\tAccount Number: {self.account_number}")

class PremiumAccounts(CheckingAccounts):
    """Sub-class of checking accounts with an additional feature."""
    def __init__(self, name, account_number):
        """Brings over attributes of Checking Accounts to be edited."""
        super().__init__(name, account_number)
        self.cash_back = '5%'

premium_0 = PremiumAccounts('jane doe', '827659')
premium_0.show_account()