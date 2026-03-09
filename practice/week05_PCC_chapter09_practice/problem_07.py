# A hotel manages room reservations in code.
# Staff need to update a guest's room number through a method
# rather than accessing the attribute directly.
#
# Create one guest and update their room number using a method.
# Print the room number before and after.

class RoomReservations:
    """Helps a hotel manage room reservations."""
    def __init__(self, name, room_number):
        self.name = name
        self.room_number = room_number
    
    def update_room(self, new_room):
        """Updates the room number for a reservation."""
        self.room_number = new_room
        print(f"You have been reassigned to Room #{self.room_number}.")
    
    def show_room(self):
        """Displays the room number assigned to a reservation."""
        print(f"You will be staying in Room #{self.room_number}.")

reservation_0 = RoomReservations('jane doe', 1244)
reservation_0.show_room()
reservation_0.update_room(1677)