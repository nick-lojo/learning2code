# ============================================================
# MINI-PROJECT SPEC: Apex Circuit — Race Team Manager
# Chapter 9: Classes | Python Crash Course
# ============================================================
#
# SCENARIO
# --------
# You're building an internal tool for a motorsport analyst.
# The tool models a racing season — teams, their drivers,
# and race results across the championship calendar.
#
# Two driver types exist: Race Drivers and Reserve Drivers.
# Both share common driver characteristics, but each has
# at least one attribute specific to their role.
#
# A Team owns its drivers and tracks its constructor points.
#
# All class definitions live in a module (or modules).
# The main script imports from that module to create
# instances and run the demo.
#
# ============================================================
# RAW DATA — Use exactly as provided.
# ============================================================
#
# TEAMS
# (team_name, engine_supplier, home_country)
#
#   "Vortex Racing",       "Meridian Power",   "Germany"
#   "Ironclad Motorsport", "Apex Engines",     "United Kingdom"
#   "Solaris GP",          "Meridian Power",   "Italy"
#
# RACE DRIVERS
# (driver_id, team, name, nationality, car_number)
#
#   "RD-01",  Vortex Racing,        "Kai Brenner",      "German",    7
#   "RD-02",  Vortex Racing,        "Luca Ferretti",    "Italian",   8
#   "RD-03",  Ironclad Motorsport,  "James Whitmore",   "British",  44
#   "RD-04",  Ironclad Motorsport,  "Seb Nakamura",     "Japanese", 45
#   "RD-05",  Solaris GP,           "Marco Reyes",      "Spanish",  11
#   "RD-06",  Solaris GP,           "Theo Laurent",     "French",   12
#
# RESERVE DRIVERS
# (driver_id, team, name, nationality, status)
#
#   "RV-01",  Vortex Racing,        "Pieter Van Hoek",  "Dutch",    "available"
#   "RV-02",  Ironclad Motorsport,  "Aiden Foley",      "Irish",    "available"
#   "RV-03",  Solaris GP,           "Ryo Tanaka",       "Japanese", "available"
#
# RACE RESULTS — Points to award to each driver after each race
# (driver_id, points_earned)
#
#   Grand Prix of Valcourt:
#     RD-01: 25,  RD-03: 18,  RD-05: 15,  RD-02: 12,
#     RD-06: 10,  RD-04: 8
#
#   Grand Prix of Stratos:
#     RD-04: 25,  RD-02: 18,  RD-06: 15,  RD-01: 12,
#     RD-03: 10,  RD-05: 8
#
# DRIVER SWAP (apply after races are logged)
#
#   RD-04 (Seb Nakamura) is ruled out injured.
#   RV-02 (Aiden Foley) steps in for Ironclad Motorsport.
#   Update RV-02 status to "active".
#
# ============================================================
# WHAT THE TOOL MUST DO
# ============================================================
#
# 1. Model a base Driver with shared attributes: driver_id,
#    name, nationality, and career points (default: 0).
#    Include a method to display a driver summary and a method
#    to add points after a race result.
#
# 2. Race Driver and Reserve Driver are specialized types.
#    Each inherits from the base Driver and adds at least one
#    attribute specific to that role.
#
# 3. A Team stores its information and maintains a roster of
#    drivers. Include a method that displays the full team
#    profile: team info, all drivers, and each driver's
#    current points total.
#
# 4. Constructor points = sum of all race driver points on
#    that team. The team should be able to report its
#    current constructor standing.
#
# 5. Support logging a race result that adds points to a
#    specific driver.
#
# 6. Support swapping a reserve driver to active status.
#
# 7. No class logic lives in the main script — it belongs
#    in the module(s).
#
# ============================================================
# SUCCESS CRITERIA
# ============================================================
#
# 1. Running the main script produces readable output showing
#    all 3 teams with their full rosters.
#
# 2. Driver points are correct after both races are logged.
#    Kai Brenner: 37pts | Luca Ferretti: 30pts
#    James Whitmore: 28pts | Seb Nakamura: 33pts
#    Marco Reyes: 23pts | Theo Laurent: 25pts
#
# 3. Constructor points are correct:
#    Vortex Racing: 67 | Ironclad Motorsport: 61 | Solaris GP: 48
#
# 4. After the driver swap, Aiden Foley's status shows "active"
#    in Ironclad's roster output.
#
# 5. Each driver type displays its type-specific attribute
#    in its summary output.
#
# 6. Code runs without errors.
#
# ============================================================