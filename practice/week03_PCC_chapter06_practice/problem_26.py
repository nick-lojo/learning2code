# You're processing job applications.
#
# Create a dictionary called applications with two applicants:
# - 'APP001': name='Sarah Lee', experience=5, skills=['Python', 'SQL']
# - 'APP002': name='Tom Wilson', experience=2
#
# Note: APP002 has no 'skills' key.
#
# For each application:
# - Print the application ID and candidate name
# - Try to print their skills list. If they didn't provide skills, print
#   'Skills not provided'
# - If they DID provide skills, print each skill on a separate line

applications = {
    'APP001':{
        'name':'Sarah Lee',
        'experience':5,
        'skills':['Python', 'SQL']
    },
    'APP002':{
        'name':'Tom Wilson',
        'experience':2
    }
}

for application_id, candidate_info in applications.items():
    no_skills = candidate_info.get('skills', 'Skills not provided')
    print(f"\nApplication ID: {application_id}")
    print(f"\tName: {candidate_info['name']}")
    print('\tSkills:')
    print(f"\t\t{no_skills}")