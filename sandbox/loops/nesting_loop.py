report = {}
reporting = True

while reporting:
    stop = input("What stop is this? ")
    name = input("What is your name? ")
    observation = input("What did you observe at this stop? ")

    report[stop] = {name:observation}

    reporting_active = input("Do you have any more stops to report? (yes / no) ")
    if reporting_active == 'no':
        reporting = False

print("\n–––Report Results–––")
for stop, details in report.items():
    print(f"Stop: {stop.title()}")
    for inspector, observation in details.items():
        print(f"\tInspector: {inspector.title()}")
        print(f"\tObservation: {observation}")