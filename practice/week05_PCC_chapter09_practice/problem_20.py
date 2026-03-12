# A hospital system stores patient records in code.
# Each patient has a primary care physician assigned to them.
# A physician's details are complex enough to track separately.
#
# Build this out and access the physician's details through the patient.

class Physician:
    """Builds a physician."""
    def __init__(self, name, specialty):
        """Attributes of a physician."""
        self.name = name
        self.specialty = specialty

class Patient:
    """Builds a patient."""
    def __init__(self, name, physician, physician_specialty):
        """Attributes of a patient."""
        self.name = name
        self.physician = Physician(physician, physician_specialty)
    
    def patient_details(self):
        """Print patient details."""
        print(f"Name: {self.name.title()}")
        print(f"\tPhysician: Dr. {self.physician.name.title()}")

patient_0 = Patient('john smith', 'johnson', 'cardiac')
patient_0.patient_details()