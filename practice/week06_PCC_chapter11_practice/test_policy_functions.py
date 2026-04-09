from problem_03 import format_policy_number as fpn

def test_format_policy():
    test_policy = fpn('zur', 112313403)
    assert test_policy == 'ZUR-112313403'