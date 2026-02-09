completed_courses = ['Intro Python','Git Basics', 'Databases']
enrollment_requests = ['Web Development', 'Intro Python', 'Testing Basics',
                       'Git Basics']
for course in enrollment_requests:
    if course in completed_courses:
        print(f'Already completed {course}')
    else:
        print(f'Enrolled in {course}')