from problem_08 import get_formatted_address as gfa

def test_with_zip():
    """Tests the output of a formatted address with a zipcode."""
    address_0 = gfa('123 main st', 'new york city', 'new york', '10001')
    assert address_0 == '123 Main St, New York City\nNew York 10001'

def test_no_zip():
    """Tests the output of a formatted address without a zipcode."""
    address_1 = gfa('456 broadway', 'new york', 'new york')
    assert address_1 == '456 Broadway, New York, New York'