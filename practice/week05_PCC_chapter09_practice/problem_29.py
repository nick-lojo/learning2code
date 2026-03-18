# A hotel tracks the nightly rate for each room.
# Management needs a way to update the rate for a specific room
# when pricing changes seasonally.
#
# Create one room and update its rate through a method.
# Print the rate before and after.

class HotelRoom:
    """Builds a model for a hotel room."""
    def __init__(self, room_number, nightly_rate):
        """Defines attributes for hotel class."""
        self.room_number = room_number
        self.nightly_rate = nightly_rate
    
    def room_details(self):
        """Shares details about a room booking."""
        message = f"\nRoom Number: {self.room_number.upper()}"
        message += f"\n\tNightly Rate: ${self.nightly_rate}"
        print(message)
    
    def seasonal_rate(self, new_rate):
        """Changes the nightly rate for seasonally pricing."""
        self.nightly_rate = new_rate
        print(f"\nDue to high demand, the nightly rate is now ${self.nightly_rate}")

room_0 = HotelRoom('c227', 250)
room_0.room_details()
room_0.seasonal_rate(350)