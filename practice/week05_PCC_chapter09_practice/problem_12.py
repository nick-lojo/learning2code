# A software company has a general employee type in their HR system.
# Senior engineers have all the same traits as general employees,
# but they handle code reviews differently than the standard process.
#
# Build this out and demonstrate the difference in behavior.

class Employee:
    """Models an employee."""
    def __init__(self, name, experience, department):
        self.name = name
        self.department = department
        self.experience = experience
    
    def handle_review(self):
        """Prints instruction for code review."""
        print("Please send your code to a senior engineer for review.")

class SoftwareEngineer(Employee):
    """A special kind of employee."""
    def __init__(self, name, experience):
        """Attributes of a software engineer,
        and attributes rolled over from the parent class."""
        super().__init__(name, experience, 'software')
    
    def handle_review(self):
        """Prints instructions for code review."""
        if self.experience == 'senior':
            print("Please submit your code to a Principal for review.")
        else:
            Employee.handle_review(self)
    
engineer_0 = SoftwareEngineer('hudson lockett', 'senior')
engineer_0.handle_review()

employee_0 = Employee('will werts', 'junior', 'marketing')
employee_0.handle_review()

engineer_1 = SoftwareEngineer('jamie dell', 'junior')
engineer_1.handle_review()