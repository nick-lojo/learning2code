def format_city(city, country, population=0):
    """Neatly formats a city, the country it is in, and its population."""
    if population == 0:
        city_info = f"{city}, {country}"
    else:
        city_info = f"{city}, {country}"
        city_info += f"\n\tPopulation: {population}"
    return city_info.title()