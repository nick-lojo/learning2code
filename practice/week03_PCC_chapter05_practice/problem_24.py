visitor_ages = [2, 8, 15, 42, 67, 5, 70, 35]

for age in visitor_ages:
    if age <= 3:
        print(f'Age {age}: Free Admission')
    elif age <= 12:
        print(f'Age {age}: $15 ticket')
    elif age <= 64:
        print(f'Age {age}: $25 ticket')
    elif age > 64:
        print(f'Age {age}: $20 senior ticket')