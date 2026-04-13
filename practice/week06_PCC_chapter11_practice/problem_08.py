# Your function get_formatted_address() takes a street, city,
# and state and returns a formatted string. It works for
# two-part addresses.
#
# You now need it to handle an optional zip code.
# You add zip as a required parameter — and your existing
# test breaks.
#
# Fix the function so the existing test still passes AND
# zip code is supported when provided.
# Write both test functions and run them.
# Paste both files and output.

def get_formatted_address(street, city, state, zip=''):
    """Formats two=part addresses into a string."""
    if zip:
        address = f'{street.title()}, {city.title()}'
        address += f'\n{state.title()} {zip}'
        print(f'Address: {address}')
    else:
        address = f'{street.title()}, {city.title()}, {state.title()}'
        print(f'Address: {address}')
    return address