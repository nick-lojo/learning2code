rsvp_list = ['Sarah', 'Marco', 'Stella', 'Regis', 'Kelly']
checkin_list = ['sarah', 'MIKE', 'Stacy', 'REGIS', 'Kelsey']
rsvp_list_lower = [name.lower() for name in rsvp_list]

for name in checkin_list:
    if name.lower() in rsvp_list_lower:
        print(f'Welcome, {name.title()}! Please come in.')
    else:
        print(f'{name.title()}, you are not on the list. Please see the coordinator.')