# A gym management system needs to track personal trainers.
# Each trainer has a name, a certification level, and a specialty.
#
# Build this and print each attribute individually using dot notation.

class PersonalTrainer:
    """Builds profiles for personal trainers at a gym."""
    def __init__(self, name, cert_level, specialty):
        """Attributes of a PT."""
        self.name = name
        self.cert_level = cert_level
        self.specialty = specialty
    
    def show_trainer(self):
        """Prints the details of a personal trainer."""
        message = f"\nName: {self.name.title()}"
        message += f"\tCertification Level: {self.cert_level}"
        message += f"\tSpecialty: {self.specialty.title()}"

trainer_0 = PersonalTrainer('jack', 4, 'cardio')
print(trainer_0.name.title())
print(trainer_0.cert_level)
print(trainer_0.specialty.title())