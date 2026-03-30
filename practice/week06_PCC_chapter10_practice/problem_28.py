# A fitness app calculates a user's daily calorie burn rate.
# It divides total calories burned by hours of activity.
# Bad input should not crash the program.
#
# Your job: prompt for both values and calculate the rate.
# Handle any bad input gracefully.

def burn_rate():
    """Calculates a user's calorie burn rate."""
    message = '\nPlease provide your total calories and hours of activity to'
    message += ' calculate your burn rate.'
    print(message)

    total_cal = input('\nHow many total calories did you burn today? ')
    active_hours = input('How many hours were you active today? ')

    try:
        burn_rate = int(total_cal) / int(active_hours)
    except ZeroDivisionError:
        print('\nActive hours must be greater than 0.')
    else:
        message = f'\nYour burn rate is {burn_rate} calories/hour.'
        print(message)

burn_rate()