# A gym membership system calculates a member's cost per visit.
# It divides total amount paid by number of visits.
# Bad input should not crash the program.
#
# Your job: prompt for both values and calculate the cost per
# visit. Handle any bad input gracefully.

def avg_cost(total, visits):
    """Calculates the cost per visist of a gym membership."""
    try:
        average_cost = int(total) / int(visits)
    except ValueError:
        message = '\nPlease make sure you enter an integer for total cost and'
        message += ' total vists. Avoid symbols i.e., $.'
        print(message)
    else:
        message = f'\nYour average cost per visit is: ${average_cost}.'
        print(message)

avg_cost('$200', 22)

avg_cost(200, 22)