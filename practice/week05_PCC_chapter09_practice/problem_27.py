# A hospital system tracks medical staff.
# Surgeons are a specific kind of staff member
# with two additional attributes that general staff don't have.
#
# Build the surgeon as an extension of general staff.
# Create one instance and confirm all attributes are accessible.

class MedicalStaff:
    """Models medical staff at a hospital."""
    def __init__(self, name, department):
        """Asssigns attributes."""
        self.name = name
        self.department = department
    
    def print_details(self):
        """Prints the details of the medical staff."""
        message = f"\nName: {self.name.title()}"
        message += f"\n\tDepartment: {self.department.title()}"
        print(message)

class Surgeon(MedicalStaff):
    """A sub-class of medical staff at a hospital."""
    def __init__(self, name, department, specialty, shift):
        """Inherits parent class and defines new attributes."""
        super().__init__(name, department)
        self.specialty = specialty
        self.shift = shift
    
    def print_details(self):
        """Prints the details of the medical staff."""
        message = f"\nName: Dr. {self.name.title()}"
        message += f"\n\tDepartment: {self.department.title()}"
        message += f"\n\tSpecialty: {self.specialty.title()}"
        message += f"\n\tShift: {self.shift}"
        print(message)

surgeon_0 = Surgeon('jane doe', 'cardiology', 'bypass surgery',
                    'MWF 6 AM - 8 PM')

surgeon_0.print_details()