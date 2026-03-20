from driver_module import RaceDriver as RD
from driver_module import ReserveDriver as RvD
from teams_module import Team

def run_display_driver(teams):
    """Runs display_driver for all drivers."""
    print(f"\n––This Season's Drivers––")
    for team in teams:
        for race_driver in team.race_drivers:
            race_driver.display_driver()
        for reserve_driver in team.reserve_drivers:
            reserve_driver.display_driver()

def run_display_team(teams):
    """Runs display team for all teams."""
    for team in teams:
        team.display_team()

def show_constructors_points(teams):
    """Prints the points teams have earned in the Constructors Championship"""
    print(f"\nConstructor's Table:")
    for team in teams:
        print(f"\t{team.team_name.title()}: {team.constructors_points}")

def show_drivers_points(teams):
    """Prints the points drivers have earned in the Drivers Championship"""
    print(f"\nDriver's Table:")
    for team in teams:
        for race_driver in team.race_drivers:
            print(f"\t{race_driver.name.title()}: {race_driver.season_points}")
        for reserve_driver in team.reserve_drivers:
            print(f"\t{reserve_driver.name.title()}: {reserve_driver.season_points}")