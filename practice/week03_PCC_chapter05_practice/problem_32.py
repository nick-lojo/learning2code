temperatures = [25, 75, -5, 90, 50]

for temperature in temperatures:
    if temperature < 0:
        print(f'Freezing alert')
    elif temperature <= 32:
        print('Very cold')
    elif temperature <= 60:
        print('Cold')
    elif temperature <= 80:
        print('Comfortable')
    else:
        print('Hot')