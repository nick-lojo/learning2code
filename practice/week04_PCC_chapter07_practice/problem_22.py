# You're building a tool for a hotel concierge.
#
# Starting from floor 1, log every floor in the building up to floor 8.
# Each line should read: "Floor [number] inspected."

floor = 1

while floor <= 8:
    print(f"Floor {floor} inspected.")
    floor = floor + 1