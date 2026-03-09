"""A module to store a class that models restaurants."""

class Restaurant:
    """Models restaurants."""
    def __init__(self, name, cuisine):
        """Attaches a name and cuisine to a restaurant."""
        self.name = name
        self.cuisine = cuisine
        self.customers_served = 0
    
    def describe_restaurant(self):
        """Prints the name and style of food for the restaurant."""
        print(f"\n{self.name.title()} serves {self.cuisine}.")

    def open_restaurant(self):
        """Prints a message that the restaurant is now open."""
        print(f"{self.name.title()} is now open!")
    
    def share_served(self):
        """Shares how many customers the restaurant has served."""
        print(f"\n{self.name.title()} has served {self.customers_served} customers.")

    def set_number_served(self, served):
        """Let's you set the number of customers served."""
        if served >= self.customers_served:
            self.customers_served = served
        else:
            print("You can't un-serve a customer!")
    
    def increment_number_served(self, serves):
        """Incrementally add to the total number of customers served."""
        self.customers_served += serves