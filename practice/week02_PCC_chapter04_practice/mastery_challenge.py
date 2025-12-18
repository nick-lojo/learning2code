roster = ['lebron', 'curry', 'durant', 'giannis', 'jokic', 'embiid',
          'tatum', 'booker']

print('Full roster:')
for player in roster:
    print(player.title())

print('\nStarting lineup:')
for player in roster[:5]:
    print(player.title())

print('\nBench players:')
for player in roster[-3:]:
    print(player.title())