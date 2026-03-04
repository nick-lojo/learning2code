# You're building a dispatch tool for a rideshare company.
#
# A list of ride requests is waiting to be assigned.
# Write a tool that accepts the list and prints each request.
# The original list must remain unchanged after the tool runs.
# Confirm this by printing the original list afterward.

def assign_requests(requests, assigned):
    """Assigns ride requests to drivers without changing original list."""
    while requests:
        processing = requests.pop(0)
        print(f"Assigning {processing} to a driver...")
        assigned.append(processing)

def assigned_rides(assigned):
    print(f"\nThe following requests have been assigned to a driver:")
    for ride in assigned:
        print(f"\t{ride}")

ride_requests = ['request_0', 'request_1', 'request_2', 'request_3']
ride_assignments = []

assign_requests(ride_requests[:], ride_assignments)
assigned_rides(ride_assignments)

print(f"\n{ride_requests}")