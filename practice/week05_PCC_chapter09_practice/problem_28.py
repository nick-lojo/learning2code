# A parking garage tracks available spaces in real time.
# When cars enter, the count changes.
# An attendant needs a way to update the current number of open spaces
# after a manual recount.
#
# Create one garage and demonstrate the update.
# Print the value before and after.

class Garage:
    """Models a garage and tracks spots."""
    def __init__(self, open_spaces=20):
        """Assigns attributes."""
        self.open_spaces = open_spaces
    
    def print_spaces(self):
        """Prints the number of open spaces in the garage."""
        print(f"\nThere are {self.open_spaces} spaces available to park in.")
    
    def count_spaces_enter(self, cars_entered):
        """Adjusts the number of open spots"""
        if self.open_spaces - cars_entered < 0:
            print("\nYou cannot have a negative number of spaces in the garage.")
        else:
            self.open_spaces -= cars_entered
            if self.open_spaces == 0:
                message = f"\nThe garage is currently full. Please block the"
                message += " entrance until a space opens up."
                print(message)
            else:
                message = f"\n{cars_entered} cars entered the garage."
                message += f" {self.open_spaces} spots are still open."
                print(message)

    def count_spaces_left(self, cars_left):
        """Adjusts the number of open spots"""
        if self.open_spaces + cars_left > 20:
            print("\nThere are only 20 total spots in the garage.")
        else:
            self.open_spaces += cars_left
            if self.open_spaces == 20:
                message = f"\nAll spaces are open."
                print(message)
            else:
                message = f"\n{cars_left} cars have left the garage."
                message += f" {self.open_spaces} spots are now open."
                print(message)

garage_0 = Garage()
garage_0.print_spaces()
garage_0.count_spaces_enter(6)
garage_0.print_spaces()
garage_0.count_spaces_left(5)
garage_0.print_spaces()
garage_0.count_spaces_enter(20)
garage_0.print_spaces()
garage_0.count_spaces_left(2)
garage_0.print_spaces()