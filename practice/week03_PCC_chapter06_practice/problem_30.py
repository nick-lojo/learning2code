# You're reviewing project assignments.
#
# Create a dictionary called projects with four team members and their
# assigned projects:
# - 'zhang': 'Database Migration'
# - 'adams': 'API Development'
# - 'baker': 'UI Redesign'
# - 'chen': 'API Development'
#
# First, print each team member and their project in alphabetical order by
# name. Then, print all unique project names being worked on (no duplicates).

projects = {
    'zhang':'Database Migration',
    'adams':'API Development',
    'baker':'UI Redesign',
    'chen':'API Development'
}

for name, project in sorted(projects.items()):
    print(f"\nName: {name.title()}")
    print(f"\tProject: {project}")

print('\nCurrent Projects:')
for project in set(projects.values()):
    print(f"\t{project}")