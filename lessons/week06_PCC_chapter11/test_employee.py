from l02_testing_classes import Employee

def test_give_default_raise():
    """Ensures that the default raise is applied."""
    employee_0 = Employee('jane', 'doe', 100000)
    employee_0.give_raise()
    assert employee_0.annual_salary == 105000

def test_give_custom_raise():
    """Ensures that a custom raise is applied."""
    employee_0 = Employee('jane', 'doe', 100000)
    employee_0.give_raise(salary_raise=10000)
    assert employee_0.annual_salary == 110000