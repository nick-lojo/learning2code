current_users = ['Sarah', 'MIKE', 'Carlos', 'emma']
new_users = ['sarah', 'Alex', 'CARLOS']
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Username "{user} is taken. Choose another')
    else:
        print(f'Username "{user}" is available')