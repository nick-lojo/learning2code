class BaseDriver:
    """Models a base driver."""
    def __init__(self, driver_id, team, name, nationality, season_points=0):
        """Attributes shared by all drivers."""
        self.driver_id = driver_id
        self.team = team
        self.name = name
        self.nationality = nationality
        self.season_points = season_points
    
    def display_diver(self):
        """A method to display details about a driver."""
        message = f"\nDriver ID: {self.driver_id}"
        message += f"\n\tTeam: {self.team.title()}"
        message += f"\n\tName: {self.name.title()}"
        message += f"\n\tNationality: {self.nationality.title()}"
        message += f"\n\tSeason Points: {self.season_points}"
        print(message)
    
    def add_points(self, place):
        """A method to add points to a driver after winning a race."""
        if place == '1st':
            self.season_points += 25
        elif place == '2nd':
            self.season_points += 18
        elif place == '3rd':
            self.season_points += 15
        elif place == '4th':
            self.season_points += 12
        elif place == '5th':
            self.season_points += 10
        elif place == '6th':
            self.season_points += 8
        
        print(f"You now have {self.season_points} points on the season.")