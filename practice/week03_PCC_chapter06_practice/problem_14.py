# You're analyzing survey responses.
#
# You have responses from different people:
# - person_a: 'python'
# - person_b: 'javascript'
# - person_c: 'python'
# - person_d: 'rust'
#
# Print all the language responses (just the values), one per line.
# Don't print the person names.

survey_responses = {
    'person_a':'python',
    'person_b':'javascript',
    'person_c':'python',
    'person_d':'rust'
}

for responses in survey_responses.values():
    print(f'{responses.title()}')