# A university needs to represent students in code.
# Each student has a name and a major.
# Two different students are enrolled this semester.
#
# Show that each student carries their own information independently.

class Students:
    """Creates students in a university database."""
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
    
    def student_info(self):
        """Prints information for each student."""
        print(f"\nStudent Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"\tMajor: {self.major.title()}")

student_0 = Students('matt', 'carsen', 'communication')
student_1 = Students('kelly', 'benson', 'computer science')

student_0.student_info()
student_1.student_info()