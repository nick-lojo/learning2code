# You're tracking office equipment assignments.
#
# Create a dictionary called assignments with three employees:
# - 'emp_001': name='Alice Chen', device='Laptop', model='ThinkPad'
# - 'emp_002': name='Bob Smith', device='Desktop', model='OptiPlex'  
# - 'emp_003': name='Carol Lee', device='Tablet', model='iPad'
#
# Loop through all assignments.
#
# For each employee, print their employee ID, name, and what device model
# they have.

assignments = {
    'emp_001':{
        'name':'Alice Chen',
        'device':'Latop',
        'model':'Thinpad'
    },
    'emp_002':{
        'name':'Bob Smith',
        'device':'Desktop',
        'model':'OptiPlex'
    },
    'emp_003':{
        'name':'Carol Lee',
        'device':'Tablet',
        'model':'iPad'
    }
}

for employee_id, employee_info in assignments.items():
    print(f"\nEmployee ID: {employee_id}")
    print(f"\tName: {employee_info['name']}")
    print(f"\tDevice Model: {employee_info['model']}")