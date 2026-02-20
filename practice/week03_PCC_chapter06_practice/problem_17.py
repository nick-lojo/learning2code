# You're tracking a student's course enrollment.
#
# Create a dictionary for a student with:
# - name: 'Maria'
# - student_id: 12345
# - courses: a list containing ['Math', 'Physics', 'Chemistry']
#
# Print the student's name.
# Then print each course they're enrolled in, one per line.

enrollment = {
    'name':'Maria',
    'student_id':12345,
    'courses':['Math','Physics', 'Chemistry']
}

print(f"Name: {enrollment['name']}")
print('Courses:')
for course in enrollment['courses']:
    print(f'\t{course}')