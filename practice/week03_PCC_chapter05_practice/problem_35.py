existing_users = ['Alice', 'BOB', 'Charlie', 'DIANA']
login_attempts = ['alice', 'Eve', 'bob']
existing_users_lower = [user.lower() for user in existing_users]

for username in login_attempts:
    if username.lower() in existing_users_lower:
        print(f'Username "{username.lower()}" is already taken')
    else:
        print(f'Username "{username.lower()}" is available')