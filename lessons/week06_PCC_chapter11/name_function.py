def get_formatted_name(first, last, middle=''):
    """Combine first and last name with a space between them."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()