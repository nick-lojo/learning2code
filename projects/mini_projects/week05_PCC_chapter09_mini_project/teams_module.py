from driver_module import RaceDriver as RD
from driver_module import ReserveDriver as RvD

class Team:
    """A class that models teams in the racing circuit."""
    def __init__(self, team_name, engine_supplier, home_country, race_drivers,
                 reserve_drivers, constructors_points=0):
        """Key attributes of the Team class."""
        self.team_name = team_name
        self.engine_supplier = engine_supplier
        self.home_country = home_country
        self.race_drivers = race_drivers
        self.reserve_drivers = reserve_drivers
        self.constructors_points = constructors_points
    
    def display_team(self):
        """A method to display details about a team."""
        message = f"\nTeam Name: {self.team_name.title()}"
        message += f"\n\tEngine Supplier: {self.engine_supplier.title()}"
        message += f"\n\tHome Country: {self.home_country.title()}"
        message += f"\n\tConstructor's Points: {self.constructors_points}"
        print(message)
        print(f"\n\t{self.team_name.title()} Drivers:")
        for racer in self.race_drivers:
            print(f"\t\t{racer.name.title()}")
        print(f"\t{self.team_name.title()} Reserve(s):")
        for reserve in self.reserve_drivers:
            print(f"\t\t{reserve.name.title()}")
    
    def update_constructors_points(self):
        """Updates the number of constructors points accumulated in a season."""
        self.constructors_points = 0
        for racer in self.race_drivers:
            self.constructors_points += racer.season_points
        for racer in self.reserve_drivers:
            self.constructors_points += racer.season_points
        message = f"\n"
        message += f"{self.team_name.title()} now has {self.constructors_points}"
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