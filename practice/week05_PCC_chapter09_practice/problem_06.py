# A gym tracks how many classes each member has attended.
# A staff member needs to manually correct a member's class count
# after discovering a data entry error.
#
# Create one member and update their count directly, without using a method.
# Print the value before and after the correction.

class Members:
    """Tracks gym members and their activity."""
    def __init__(self, first_name, last_name, class_count):
        self.first_name = first_name
        self.last_name = last_name
        self.class_count = class_count

    def classes_attended(self):
        """Displays the number of classes attended by a gym member."""
        print(f"{self.first_name.title()} has attended {self.class_count} classes.")

member_0 = Members('max', 'arroyo', 4)
member_0.classes_attended()
member_0.class_count = 6
member_0.classes_attended()