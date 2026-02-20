# You're managing a todo list stored as a dictionary.
#
# Start with these tasks:
# - 'task_1': 'Buy groceries'
# - 'task_2': 'Clean room'
# - 'task_3': 'Study Python'
#
# You completed 'task_2'.
# Remove it from the dictionary.
#
# Print the dictionary to show the remaining tasks.

todo_list = {
    'task_1':'Buy groceries',
    'task_2':'Clean room',
    'task_3':'Study Python'
}

del(todo_list['task_2'])

print(todo_list)