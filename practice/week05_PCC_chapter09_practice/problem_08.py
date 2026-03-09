# A coffee shop tracks how many stamps a customer has on their loyalty card.
# Each time a customer makes a purchase, their stamp count goes up by one.
# Customers can make multiple purchases in a single visit.
#
# Create one customer and simulate a visit where they make 3 purchases.
# Print the stamp count after each purchase.

class CustomerProfile:
    """Builds a customer profile for a coffee shop."""
    def __init__(self, name, loyalty_stamps):
        self.name = name
        self.loyalty_stamps = loyalty_stamps
    
    def update_loyalty_stamps(self, purchases):
        """Updates the number of loyalty stamps on a customers' card based on their purchases."""
        if purchases == 1:
            self.loyalty_stamps += purchases
            print(f"Your loyalty card has been stamped {purchases} time.")
        elif purchases > 1:
            self.loyalty_stamps += purchases
            print(f"You made {purchases} this visit. Your card has been stamped {purchases} times.")
        else:
            print("You must make a purchase to have your card stamped.")
    
    def show_profile(self):
        """Displays the customer's name and card stamps."""
        print(f"\n Customer Name: {self.name.title()}")
        print(f"\tLoyalty Stamps: {self.loyalty_stamps}")

customer_0 = CustomerProfile('jane doe', 2)
customer_0.update_loyalty_stamps(1)
customer_0.update_loyalty_stamps(1)
customer_0.update_loyalty_stamps(1)

customer_0.show_profile()