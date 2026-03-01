# MINI-PROJECT: Pro Football Draft Board Manager
#
# SCENARIO:
# You're a scout for a pro football team managing a pre-draft prospect board.
# Some prospects have been flagged as ineligible and must be removed
# before the team begins making selections.
#
# RAW DATA (build your own data structures from this):
#
# Prospect board (in order): # I just want to clarify that Claude Sonnet 4.6 came up with these names, not me
#   Jaylon Carter, Marcus Webb, Devon Stills, Marcus Webb,
#   Trey Harmon, Isaiah Ford, Marcus Webb, Cole Pickett,
#   Darius Lane, Trey Harmon
#
# Ineligible prospect: Marcus Webb (appears multiple times — all instances
# must be removed)
#
# WHAT TO BUILD:
# 1. Before selections begin, remove all instances of the ineligible prospect
#    from the board and print a notice each time one is removed
# 2. Work through the remaining prospects one at a time, moving each from the
#    board to a selected list and printing a confirmation for each
# 3. After all prospects are selected, collect scouting notes:
#    - Prompt for a prospect name and a brief note
#    - Store each note linked to the prospect
#    - Keep collecting until the scout signals they are done
# 4. Print a final summary of all scouting notes

prospect_board = ['Jaylon Carter', 'Marcus Webb', 'Devon Stills', 'Marcus Webb',
                  'Trey Harmon', 'Isaiah Ford', 'Marcus Webb', 'Cole Pickett',
                  'Darius Lane', 'Trey Harmon']

while 'Marcus Webb' in prospect_board:
    prospect_board.remove('Marcus Webb')

prospect_board = set(prospect_board)
prospect_board = list(prospect_board)
print(f"\nTotal Prospects: {len(prospect_board)}")
print(f"{prospect_board}\n")

drafted = []

while prospect_board:
    selected = prospect_board.pop()
    print(f"{selected} has been drafted.")
    drafted.append(selected)

print(f"\nTotal Picks: {len(drafted)}")
for player in drafted:
    print(f"\t{player}")

if len(drafted) == 6 and len(prospect_board) == 0: # Quick check
    print("\nDrafted list built correctly.\n")
else:
    print("\nError: Not all prospects were drafted.\n")

# Everything up to here is good so far

scouting_notes = {}
collecting_notes = True

while collecting_notes:
    for player in drafted:
        name = player
        notes = input(f"What notes do you have for {name}? ")
        scouting_notes[name] = notes
        print(f"\nPlayer logged in scouting notes: {len(scouting_notes)}")
        still_collecting = input("\nHave you collected notes on all 6 players? (yes / no) ")
        if still_collecting == 'yes':
            collecting_notes = False

print("\n–––Final Summary–––")
for name, notes in scouting_notes.items():
    print(f'\t{name.title()}: "{notes}"')