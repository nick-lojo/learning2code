#This is just to see if ChatGPT Study and Learn is better than
# Claude

#Problem 1

age = 17
has_parental_consent = True

if age >= 18:
    print('Access granted.')
elif has_parental_consent == True:
    print('Access granted with conset.')
else:
    print('Access denied.')

#Problem 2
usernames = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')