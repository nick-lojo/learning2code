# A hospital system tracks medical devices in code.
# One of those devices has a component so detailed
# that it makes more sense to model it separately
# rather than pile everything into one place.
#
# Create one device and interact with its component through it.

class Component:
    """A class to be used as an attribute for medical devices."""
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def update_weight(self, new_weight):
        """Updates the weight of the component."""
        self.weight = new_weight
        print(f"The {self.name.title()}'s weight has been updated to {self.weight}g.")

class Devices:
    """Used for hospitals to track medical devices."""
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.components = Component('lazer', 200)

    def device_details(self):
        """Prints the details about the device."""
        print(f"{self.manufacturer.title()} {self.model.title()}")
        print(f"The {self.components.name.title()} is a critical component weighing {self.components.weight}g")

device_0 = Devices('techbio', 'incisionist')
device_0.device_details()
device_0.components.update_weight(300)
device_0.device_details()