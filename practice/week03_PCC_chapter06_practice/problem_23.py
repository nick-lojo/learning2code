# You're managing a simple grade book.
#
# Create a dictionary of students and their test scores:
# - 'Alex': 85
# - 'Jordan': 92
# - 'Casey': 78
# - 'Morgan': 88
#
# Print each student's name and score in alphabetical order by name.
# Then print only the unique scores that appear (no duplicates).

test_scores = {
    'Alex':85,
    'Jordan':92,
    'Casey':78,
    'Morgan':88
}

for name, score, in sorted(test_scores.items()):
    print(f"\nName: {name}")
    print(f"\tTest Score: {score}")

for score in set(test_scores.values()):
    print(score)