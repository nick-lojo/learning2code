from problem_09 import shipping_calculator as sc

def test_ground():
    """Tests that the function works for weight_lbs < 10."""
    package_0 = sc(6)
    assert package_0 == 'ground'

def test_freight():
    """Tests that the function works for weight_lbs = 10-50."""
    package_1 = sc(32)
    assert package_1 == 'freight'

def test_oversized():
    """Tests that the function works for weight_lbs > 50."""
    package_2 = sc(87)
    assert package_2 == 'oversized'