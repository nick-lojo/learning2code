from l02_testing_classes import Employee

import pytest

@pytest.fixture
def employee_0():
    """An employee that will be available to test all fixtures."""
    employee_0 = Employee('jane', 'doe', 100000)
    return employee_0

def test_give_default_raise(employee_0):
    """Tests that the default raise is applied correctly."""
    employee_0.give_raise()
    assert employee_0.annual_salary == 105000

def test_give_custom_raise(employee_0):
    """Tests that a custoom raise is applied correctly."""
    employee_0.give_raise(salary_raise=10000)
    assert employee_0.annual_salary == 110000