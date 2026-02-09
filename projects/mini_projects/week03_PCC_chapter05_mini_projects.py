player_actions = ['jump', 'throw', 'dodge', 'pick up', 'eat',
                  'deal damage', 'take damage', 'kill enemy',
                  'block', 'blocked']

print('Basic Actions Tutorial\n')

total_points = 0
print(f'Current Points: {total_points}\n')

for action in player_actions:
    if action == 'jump':
        print(f'{action.title()} is worth 5 points')
        total_points = total_points + 5
        print(f'Current Points: {total_points}\n')
    elif action == 'throw':
        print(f'{action.title()} is worth 10 points')
        total_points = total_points + 10
        print(f'Current Points: {total_points}\n')
    elif action == 'dodge':
        print(f'{action.title()} is worth 15 points')
        total_points = total_points + 15
        print(f'Current Points: {total_points}\n') 
    elif action == 'pick up':
        print(f'{action.title()} is worth 20 points')
        total_points = total_points + 20
        print(f'Current Points: {total_points}\n')
    elif action == 'eat':
        print(f'{action.title()} is worth 25 points')
        total_points = total_points + 25
        print(f'Current Points: {total_points}\n')
    elif action == 'deal damage':
        print(f'{action.title()} is worth 30 points')
        total_points = total_points + 30
        print(f'Current Points: {total_points}\n')
    elif action == 'take damage':
        print(f'{action.title()} is worth -30 points')
        total_points = total_points - 30
        print(f'Current Points: {total_points}\n')
    elif action == 'kill enemy':
        print(f'{action.title()} is worth 100 points')
        total_points = total_points + 100
        print(f'Current Points: {total_points}\n')
    elif action == 'block':
        print(f'{action.title()} is worth -10 points')
        total_points = total_points - 10
        print(f'Current Points: {total_points}\n')
    elif action == 'blocked':
        print(f'{action.title()} is worth -15 points')
        total_points = total_points - 15
        print(f'Current Points: {total_points}\n')

print(f'Tutorial Complete. Total Points: {total_points}')
print('Reset Current Points to 0.')
total_points = 0
print(f'Current Points: {total_points}\n')

print("That concludes the tutorial. Let's play the game.\n")

jumped = False
threw = False
dodged = False
picked_up = False
ate = False
dealt_damage = False
took_damage = False
killed_enemy = False
blocked_enemy = False
was_blocked = False

game_actions = ['pick up', 'jump', 'dodge', 'deal damage',
                'take damage', 'blocked', 'block', 'deal damage',
                'dodge', 'deal damage', 'block', 'deal damage', 'kill enemy']

for action in game_actions:
    if action == 'jump':
        jumped = True
        print(f'{action.title()}! +5 points!')
        total_points = total_points + 5
        print(f'Current Points: {total_points}\n')
    elif action == 'throw':
        threw = True
        print(f'{action.title()}! +10 points!')
        total_points = total_points + 10
        print(f'Current Points: {total_points}\n')
    elif action == 'dodge':
        dodged = True
        print(f'{action.title()}! +15 points!')
        total_points = total_points + 15
        print(f'Current Points: {total_points}\n') 
    elif action == 'pick up':
        picked_up = True
        print(f'{action.title()} weapon! +20 points!')
        total_points = total_points + 20
        print(f'Current Points: {total_points}\n')
    elif action == 'eat':
        ate = True
        print(f'{action.title()} food! +25 points!')
        total_points = total_points + 25
        print(f'Current Points: {total_points}\n')
    elif action == 'deal damage':
        dealt_damage = True
        print(f'{action.title()}! +30 points!')
        total_points = total_points + 30
        print(f'Current Points: {total_points}\n')
    elif action == 'take damage':
        took_damage = True
        print(f'{action.title()}! -30 points!')
        total_points = total_points - 30
        print(f'Current Points: {total_points}\n')
    elif action == 'kill enemy':
        killed_enemy = True
        print(f'{action.title()}! +100 points')
        total_points = total_points + 100
        print(f'Current Points: {total_points}\n')
    elif action == 'block':
        blocked_enemy = True
        print(f'{action.title()}! -10 points!')
        total_points = total_points - 10
        print(f'Current Points: {total_points}\n')
    elif action == 'blocked':
        was_blocked = True
        print(f'{action.title()}! -15 points!')
        total_points = total_points - 15
        print(f'Current Points: {total_points}\n')

if 'eat' not in game_actions:
        print('You never ate. -25 points for hunger.')
        total_points = total_points - 25
        print(f'Current Score: {total_points}\n')
if 'throw' in game_actions:
    print('Throw Stealth Bonus! +20 points!')
    total_points = total_points + 20
    print(f'Current Points: {total_points}\n')

if jumped and dodged:
    print('Jump-Dodge Combo! +20 points')
    total_points = total_points + 20
    print(f'Current Points: {total_points}\n')
if dodged and dealt_damage:
    print('Dodge Counter Attack! +45 points!')
    total_points = total_points + 45
    print(f'Current Points: {total_points}\n')
if blocked_enemy and dealt_damage:
    print('Block Counter Attack! +40 points!\n')
    total_points = total_points + 40
    print(f'Current Points: {total_points}')
if killed_enemy or total_points >= 1000:
    print('Game Over, You Win!\n')
    print(f'Final Score: {total_points}')
if killed_enemy == False and total_points < 0:
    print('Game Over, You Lose!\n')

print('Thanks for playing! Want to play again?')