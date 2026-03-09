# A hospital system needs to represent patients in code.
# Each patient has a name and a date of birth.
# When you ask a patient to introduce themselves,
# they should state both pieces of information.
#
# Create one patient and have them introduce themselves.

class Patients:
    """Used to build patients in a hospital database."""
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        
    def patient_info(self):
        """Prints the patients name and DOB."""
        print(f"\nPatient Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"\tDOB: {self.dob}")

patient_0 = Patients('junior', 'wilson', '04/01/1972')
patient_0.patient_info()