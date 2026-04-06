from city_functions import format_city

def test_city_functions_no_population():
    """Does a city like 'Santiago, Chile' work?"""
    formatted_city = format_city('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_city_functions_w_population():
    """Does a city like 'Santiago, Chile' work with a population of 5000000?"""
    formatted_city = format_city('santiago', 'chile', 5000000)
    assert formatted_city == 'Santiago, Chile\n\tPopulation: 5000000'