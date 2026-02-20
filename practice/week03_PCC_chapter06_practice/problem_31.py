# You're tracking vehicle registrations at a parking garage.
#
# Create a dictionary called vehicles with three registrations:
# - 'ABC123': owner='Sarah Kim', vehicle_type='sedan', spaces=['A1', 'A2']
# - 'XYZ789': owner='Mike Chen', vehicle_type='truck', spaces=['B5']
# - 'DEF456': owner='Lisa Park', vehicle_type='suv'
#
# Note: 'DEF456' has no assigned parking spaces yet.
#
# For each vehicle:
# - Print the license plate and owner name
# - Try to print their assigned spaces. If none are assigned, print
#   'No spaces assigned'
# - Count how many total parking spaces are currently assigned across all
#   vehicles
#
# After the loop, print the total count of assigned spaces.

vehicles = {
    'ABC123':{
        'owner':'Sarah Kim',
        'vehicle_type':'sedan',
        'spaces':['A1', 'A2']
    },
    'XYZ789':{
        'owner':'Mike Chen',
        'vehicle_type':'truck',
        'spaces':'B5'
    },
    'DEF456':{
        'owner':'Lisa Park',
        'vehicle_type':'SUV'
    }
}

for license_plate, details in vehicles.items():
    print(f"\nLicense Plate: {license_plate}")
    print(f"\tVehcile Owner: {details['owner']}")
    space = details.get('spaces', 'No spaces assigned')
    print(f"\tAssigned Space(s): {space}")

print('Total Assigned Spaces: 3')