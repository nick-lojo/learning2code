from problem_05 import get_risk_tier as grt

def test_get_risk_tier():
    """Confirms get_risk_tier function is working."""
    risk_tier = grt(50)
    assert risk_tier == 'standard'