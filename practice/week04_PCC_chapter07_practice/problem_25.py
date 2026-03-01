# You're building a screening tool for a job application portal.
#
# Ask the applicant for their years of experience.
# If they have 3 or more years, print that they qualify for the senior track.
# If they have less than 3, print that they qualify for the junior track.

prompt = "How many years of experience do you have? "
experience = input(prompt)
experience = int(experience)

if experience >= 3:
    print('Based on your experience, you qualify for the senior track.')
else:
    print('You qualify for the junior track.')