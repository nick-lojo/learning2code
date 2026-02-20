# You're reviewing employee records alphabetically.
#
# You have an employees dictionary with their departments:
# - zhang: 'engineering'
# - adams: 'sales'
# - chen: 'marketing'
# - baker: 'engineering'
#
# Print each employee name in alphabetical order, one per line.
# Don't print the departments.

employee_departments = {
    'zhang':'engineering',
    'adams':'sales',
    'chen':'marketing',
    'baker':'engineering'
}

for name in sorted(employee_departments.keys()):
    print(f"{name.title()}")