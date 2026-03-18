from driver_module import RaceDriver as RD
from driver_module import ReserveDriver as RvD

class Team:
    """A class that models teams in the racing circuit."""
    def __init__(self, team_name, engine_supplier, home_country, race_drivers,
                 reserve_drivers, constructors_points=0):
        self.team_name = team_name
        self.engine_supplier = engine_supplier
        self.home_country = home_country
        self.race_drivers = race_drivers
        self.reserve_drivers = reserve_drivers
        self.constructors_points = constructors_points
    
    def update_constructors_points(self):
        """Updates the number of constructors points accumulated in a season."""
        for racer in self.race_drivers:
            self.constructors_points += racer.season_points
        for racer in self.reserve_drivers:
            self.constructors_points += racer.season_points
        message = f"{self.team_name.title()} now has {self.constructors_points}"
        message += f" constructors points."
        print(message)
    
    def swap_drivers(self, old_driver, old_reserve, new_driver, new_reserve):
        """Swaps a race driver for a reserve driver."""
        self.race_drivers.remove(old_driver)
        self.reserve_drivers.remove(old_reserve)
        old_reserve.status='active'
        self.race_drivers.append(new_driver)
        self.reserve_drivers.append(new_reserve)
    
        print(f"\nThe swap is done. Here are the new race drivers:")
        for driver in self.race_drivers:
            print(f"\t{driver.name.title()}")
        print(f"\nAnd here are the new reserves:")
        for driver in self.reserve_drivers:
            print(f"\t{driver.name.title()}")