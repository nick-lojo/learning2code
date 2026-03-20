from driver_module import RaceDriver as RD
from driver_module import ReserveDriver as RVD
from teams_module import Team
from functions_module import run_display_driver as RDD
from functions_module import run_display_team as RDT
from functions_module import show_constructors_points as SCP
from functions_module import show_drivers_points as SDP

racer_0 = RD('RD-01', 'vortex racing', 'kai brenner', 'german', 7)
racer_1 = RD('RD-02', 'vortex racing', 'luca ferretti', 'italian', 8)
racer_2 = RD('RD-03', 'ironclad motorsport', 'james whitmore', 'british', 44)
racer_3 = RD('RD-04', 'ironclad motorsport', 'seb nakamura', 'japanese', 45)
racer_4 = RD('RD-05', 'solaris gp', 'marco reyes', 'spanish', 11)
racer_5 = RD('RD-06', 'solaris gp', 'theo laurent', 'french', 12)

reserve_0 = RVD('RV-01', 'vortex racing', 'pieter van hoek', 'dutch',
                'available')
reserve_1 = RVD('RV-02', 'ironclad motorsport', 'aiden foley', 'irish',
                'available')
reserve_2 = RVD('RV-03', 'solaris gp', 'ryo tanaka', 'japanese',
                'available')

team_0 = Team('vortex racing', 'meridian power', 'germany',
              [racer_0, racer_1], [reserve_0])
team_1 = Team('ironclad motorsport', 'apex engine', 'united kingdom',
              [racer_2, racer_3], [reserve_1])
team_2 = Team('solaris gp', 'meridian power', 'italy',
              [racer_4, racer_5], [reserve_2])

racing_teams = [team_0, team_1, team_2]

RDT(racing_teams)
RDD(racing_teams)

racer_0.add_points('1st')
racer_2.add_points('2nd')
racer_4.add_points('3rd')
racer_1.add_points('4th')
racer_5.add_points('5th')
racer_3.add_points('6th')

team_0.update_constructors_points()
team_1.update_constructors_points()
team_2.update_constructors_points()

SCP(racing_teams)
SDP(racing_teams)

reserve_3 = RVD(racer_3.driver_id, racer_3.team, racer_3.name, racer_3.nationality,
                'injured', season_points=racer_3.season_points)
racer_6 = RD(reserve_1.driver_id, reserve_1.team, reserve_1.name,
              reserve_1.nationality, racer_3.car_number,
              season_points=reserve_1.season_points)

team_1.swap_drivers(racer_3, reserve_1, racer_6, reserve_3)
RDT(racing_teams)

racer_6.add_points('1st')
racer_1.add_points('2nd')
racer_5.add_points('3rd')
racer_0.add_points('4th')
racer_2.add_points('5th')
racer_4.add_points('6th')

team_0.update_constructors_points()
team_1.update_constructors_points()
team_2.update_constructors_points()

SCP(racing_teams)
SDP(racing_teams)