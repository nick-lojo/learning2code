# You're building a vehicle registration tool for a DMV database.
#
# Write a tool that always accepts a make and model, plus any number
# of additional labeled details about the vehicle.
# Register one vehicle with at least two extra details and print the result.

def vehicle_registration(make, model, **vehcile_details):
    """Registers vehicles into the DMVs data base."""
    vehcile_details['make'] = make.title()
    vehcile_details['model'] = model.title()
    return vehcile_details

vehicle_0 = vehicle_registration('tesla', 'model 3',
                                 license_plate='ABE*123',
                                 address='123 Main Street')

print(vehicle_0)