#PEP 8 - Python Enhancement Proposal 8
#Official style guide for Python code

#Key rules:
#1. Indentation: Use 4 spaces per level (not tabs)
#2. Line length: Max 79 characters per line
#3. Blank lines: Use to group related code visually
#4. Comments: Max 72 characters per line

#Good indentation example
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait tp see your next trick, {magician.title()}.\n")

print('Thank you, everyone. That was a great magic shiow!')

#Blank lines separate logical sections
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('First three players:')
for player in players[:3]:
    print(player.title())