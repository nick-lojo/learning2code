# A retail company has a general product type in their system.
# Digital downloads are a specific kind of product.
# The way digital downloads are delivered is completely different
# from how the parent handles delivery.
#
# Build this out and show that the child's delivery behavior
# replaces the parent's entirely.

class GeneralProducts:
    """Builds general products for a company."""
    def __init__(self, name, price, sku):
        """Assigns attributes to the product."""
        self.name = name
        self.price = price
        self.sku = sku
    
    def delivery(self):
        """Method for printing delivery details."""
        print(f"\nYour {self.name.title()} will be delivered in 5 business days by mail.")

class DigitalDownloads(GeneralProducts):
    """A special type of product with unique delivery."""
    def __init__(self, name, price, file_type, sku=None):
        """Defines existing parameters and builds new ones."""
        super().__init__(name, price, sku)
        self.file_type = file_type
    
    def delivery(self):
        """Special delivery method for digital downloads."""
        print(f"\nWe have emailed you your {self.file_type.upper()} to download your {self.name.title()}.")

product_0 = GeneralProducts('smart phone', 599, 88673)
product_0.delivery()

digi_download_0 = DigitalDownloads('dj studio', 200, '.zip')
digi_download_0.delivery()