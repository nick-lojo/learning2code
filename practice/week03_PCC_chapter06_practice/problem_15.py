# You're analyzing the survey responses from Problem #14.
#
# Same responses:
# - person_a: 'python'
# - person_b: 'javascript'
# - person_c: 'python'
# - person_d: 'rust'
#
# Print each unique language mentioned (no duplicates).
# The languages can print in any order.

survey_responses = {
    'person_a':'python',
    'person_b':'javascript',
    'person_c':'python',
    'person_d':'rust'
}

for response in set(survey_responses.values()):
    print(f'{response.title()}')