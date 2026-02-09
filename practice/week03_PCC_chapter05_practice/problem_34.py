senders =['alice', 'spam_bot', 'bob', 'spam_bot']

for sender in senders:
    if sender != 'spam_bot':
        print(f'Message delivered from {sender.title()}')
    else:
        print('Message blocked')