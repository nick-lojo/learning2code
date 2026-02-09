registered_emails = ['Alice@email.com', 'BOB@email.com', 'charlie@EMAIL.com']
signup_attempts = ['alice@email.com', 'diana@email.com', 'BOB@EMAIL.COM']
registered_emails_lower = [email.lower() for email in registered_emails]

for email in signup_attempts:
    if email.lower() in registered_emails_lower:
        print(f'{email} is already registered')
    else:
        print(f'{email} successfully registered')