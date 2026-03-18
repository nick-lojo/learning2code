# A bank has a general account type.
# Business accounts work like general accounts
# but have three additional attributes that personal accounts don't have.
#
# Build the business account as an extension of the general account.
# Create one instance and confirm all attributes are accessible.

class GeneralAccount:
    """Models a bank account."""
    def __init__(self, name, account_type, account_number):
        """Assign attributes."""
        self.name = name
        self.account_type = account_type
        self.account_number = account_number
    
    def account_details(self):
        """Prints account details."""
        message = f"\nAccount Number: {self.account_number}"
        message += f"\n\tAccount Holder: {self.name.title()}"
        message += f"\n\tAccount Type: {self.account_type.title()}"
        print(message)
    
class BusinessAccount(GeneralAccount):
    """A special kind of bank account."""
    def __init__(self, name, account_type, account_number, account_manager,
                 accountant, expense_approver):
        """Define common attributes and unique attributes."""
        super().__init__(name, account_type, account_number)
        self.account_manager = account_manager
        self.accountant = accountant
        self.expense_approver = expense_approver
    
    def business_details(self):
        """Prints details about the business account."""
        message = f"\nAccount Manager: {self.account_manager.title()}"
        message += f"\n\tAccountant: {self.accountant.title()}"
        message += f"\n\tExpense Approver: {self.expense_approver.title()}"
        print(message)

biz_account_0 = BusinessAccount('prim & proper lawncare', 'business checkings',
                                793429876, 'jane doe', 'john smith', 'deb jones')

biz_account_0.account_details()
biz_account_0.business_details()