# You're building an HR tool to track employee information.
#
# Your system stores employees like this:
# - Each employee has: name, department, salary, years_employed
#
# Rules:
# - New employees start at salary $50,000
# - Employees in 'engineering' department get $10,000 added to base
# - For every year employed beyond 2 years, add $5,000 to salary
# - Calculate and store final salary for each employee
#
# Build the system for these employees:
# - Alice: engineering, 3 years
# - Bob: sales, 1 year  
# - Carol: engineering, 5 years
#
# Print each employee's name and their calculated final salary.

employees = {
    'alice':{
        'department':'engineering',
        'tenure':3
    },
    'bob':{
        'department':'sales',
        'tenure':1
    },
    'carol':{
        'department':'engineering',
        'tenure':5
    }
}

for employee, info in employees.items():
    salary = 50000
    department = f"{info['department']}"
    tenure = info['tenure']

    if department == 'engineering':
        salary = salary + 10000
    else:
        salary = salary
    if tenure > 2:
        salary = salary + (tenure - 2) * 5000
    else:
        salary = salary

    print(f"\nEmployee: {employee.title()}")
    print(f"\tDepartment: {department.title()}")
    print(f"\tTenure: {tenure} years")
    print(f"\tSalary: ${salary}")