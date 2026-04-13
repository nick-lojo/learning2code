# A shipping calculator returns a carrier label based on
# package weight: 'ground' under 10 lbs, 'freight' 10–50 lbs,
# 'oversized' above 50 lbs.
#
# Write the function in problem_09.py.
# Write a test file with three test functions — one per label.
# All three should pass.
# Paste both files and output.

def shipping_calculator(weight_lbs):
    """Uses the pacages weight to determine its carrier label."""
    if weight_lbs < 1:
        print("The package cannot be weightless.")
    elif weight_lbs < 10:
        carrier_label = 'ground'
        message = f'This package is {weight_lbs} lbs.'
        message += f'\nIt will be shipped via our {carrier_label} service.'
        print(message)
    elif weight_lbs < 50:
        carrier_label = 'freight'
        message = f'This package is {weight_lbs} lbs.'
        message += f'\nIt will be shipped via our {carrier_label} service.'
        print(message)
    else:
        carrier_label = 'oversized'
        message = f'This package is {weight_lbs} lbs.'
        message += f'\nIt will be shipped via our {carrier_label} service.'
    return carrier_label