# You're building a report tool for a warehouse safety inspector.
#
# The inspector needs to log observations during a walkthrough.
# The tool should run continuously across multiple stops.
# At each stop, collect the inspector's name and their observation.
# After each entry, ask if there are more stops to log.
# Print all observations when the walkthrough is complete.

report = {}
reporting = True

while reporting:
    name = input("What is your name? ")
    observation = input("What did you observe at this stop? ")

    report[name] = observation

    reporting_active = input("Do you have any more stops to report? (yes / no) ")
    if reporting_active == 'no':
        reporting = False

print("\n–––Report Results–––")
for name, observation in report.items():
    print(f'\t{name.title()} reports: "{observation}"')