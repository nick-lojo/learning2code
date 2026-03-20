from base_driver_module import BaseDriver as BD

class RaceDriver(BD):
    """A special class of base drivers."""
    def __init__(self, driver_id, team, name, nationality, car_number, season_points=0):
        """Defines attributes of the parent class and special attributes of the sub-class."""
        super().__init__(driver_id, team, name, nationality, season_points)
        self.car_number = car_number
     
    def display_driver(self):
         """A special version that includes car number."""
         super().display_driver()
         print(f"\tCar Number: #{self.car_number}")

class ReserveDriver(BD):
    """A special class of base drivers."""
    def __init__(self, driver_id, team, name, nationality, status, season_points=0):
        """Defines common attributes and defines new ones."""
        super().__init__(driver_id, team, name, nationality, season_points)
        self.status = status
    
    def display_driver(self):
        """A special version of display driver to show status."""
        super().display_driver()
        print(f"\tStatus: {self.status.title()}")