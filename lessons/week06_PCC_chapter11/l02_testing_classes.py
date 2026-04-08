# A Variety of Assertions (PCC, pg. 217-218)

# assert can check more than just equality
# assert a == b: two values are equal
# assert a != b: two values are not equal
# assert a: a evaluates to True
# assert not a: evaluates to False
# assert element in list: element is in a list
# assert element not in list: element is not in a list

# Testing a Class (PCC, pg. 218-220)

# Testing a class works similarly to testing a function
# You test the behavior of the class's METHODS
# To test a class, you need to create an instance of it first
#   then call methods on the instance and assert the results

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)
    
    def store_responses(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

# This is what manually testing the class looks like
# Create an instance, call methods, visually verify output
# Works but requires human eyes every time the class changes

# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)
# language_survey.show_question()

# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     language_survey.store_responses(response)

# print("\nThank you to everyone who participated in the survey!")
# language_survey.show_results()

# Testing the Anonymous Survey Class (PCC, pg. 220)
# Create an instance of the class inside the test function
# Call the methods on the instance
# assert the expected result

# def test_store_single_response (): # Runs in test_survey.py
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_responses('English')
#     assert 'English' in language_survey.responses

# test_store_three_responses (PCC, pg. 220-221)
# Create a list of responses, loop to store them all
# Second loop asserts every response made it into the list
# Tests can loop just like regular code

# def test_store_three_responses(): # Runs in test_survey.py
#     """Test that three individual responses are stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_responses(response)
#     for response in responses:
#         assert response in language_survey.responses

# Using Fixtures (PCC, pg. 221-223)

# Problem: we're creating a new AnonymousSurvey instance in every
#   test function - repetitive and hard to maintain at scale
# fixture: a function that sets up a resource used by multiple tests
# @pytest.fixture decorator tells pytest to run this function
#   automatically and pass its return value to any test function
#   that lists it as a parameter
# fixture name must match the parameter name in the test function

# @pytest.fixture # Runs in test_survey.py
# def language_survey():
#     """A survey that will be available to test all functions."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     return language_survey

# def test_store_single_response(language_survey):
#     """Test that a single response is stored properly."""
#     language_survey.store_responses('English')
#     assert 'English' in language_survey.responses

# def test_store_three_responses(language_survey):
#     """Test that three individual responses as stored properly."""
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_responses(response)
#     for response in responses:
#         assert response in language_survey.responses

# TRY IT YOURSELF

# 11-3. Employee: Write a class called Employee. The __init__() method
# should take in a first name, a last name, and an annual salary, and
# store each of these as attributes. Write a method called give_raise()
# that adds $5,000 to the annual salary by default but also accepts a
# different raise amount.
# Write a test file for Employee with two test functions,
# test_give_default_raise() and test_give_custom_raise(). Write your
# tests once without using a fixture, and make sure they both pass.
# Then write a fixture so you don't have to create a new employee
# instance in each test function. Run the tests again, and make sure
# both tests still pass.

class Employee:
    """Builds instances of employees."""
    def __init__(self, first_name, last_name, annual_salary):
        """Defines the attributes of the class."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_raise=5000):
        """Raises the annual salary of an employee by a default of $5,000."""
        self.annual_salary += salary_raise
        print(f"\nYou have received a raise of {salary_raise}!")
        print(f"Your annual salary is now {self.annual_salary}.")

# See test_employee.py and test_employee_fixture.py for solution.