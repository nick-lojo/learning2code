# A logistics company tracks shipments in code.
# Overnight shipments are a specific kind of shipment
# with their own attributes and behaviors.
#
# Build the overnight shipment as an extension of the general shipment.
# Create one instance and confirm it has access to the parent's behavior.

class Shipments:
    """Builds shipments for a logistics company."""
    def __init__(self, tracking_number, destination, origin, method):
        """Defines the attributes of the class."""
        self.tracking_number = tracking_number
        self.destination = destination
        self.origin = origin
        self.method = method
    
    def show_details(self):
        """Prints the details of a shipment."""
        message = f"\nShipment #{self.tracking_number} will be delivered to "
        message += f"{self.destination.title()} from {self.origin.title()} "
        message += f"by {self.method}."
        print(message)

class OvernightShipments(Shipments):
    """Models a special class of shipments."""
    def __init__(self, tracking_number, destination, origin, method, shipment_time=24):
        """Defines attributes for this class, and brings over common
        attributes from parent class."""
        super().__init__(tracking_number, destination, origin, method)
        self.shipment_time = shipment_time
    
    def overnight_details(self):
        """Additional details for overnight shipping."""
        print(f"\tThis is an overnight shipment. It must be delivered within {self.shipment_time} hours.")

shipment_0 = Shipments(9823748, 'kansas city', 'los angeles', 'rail')
shipment_0.show_details()

shipment_1 = OvernightShipments(82467364, 'charlottesville', 'newark', 'air')
shipment_1.show_details()
shipment_1.overnight_details()