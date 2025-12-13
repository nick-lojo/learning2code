#Slicing - working with a specific portion of a list
#Format: list[start:stop] = stops BEFORE the stop index

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #First three players (indices 0, 1 ,2)

#Slice indices 1 through 3 (second, third, fourth)
print(players[1:4])

#Omit the first index - Python starts at the beginning
print(players[:4])

#Omit the second index - Python goes to the end
print(players[2:])

#Negative indices - count from the end
print(players[-3:])

#Loop through a slice instead of the entire list

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#Copying a list using a slice [:]

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #Creates a copy

#Add different items to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods:')
print(my_foods)

print("\nMy friend's favorite foods:")
print(friend_foods)

#WRONG WAY - this doesn't copy, it creates a second reference to the same list

my_foods_wrong = ['pizza', 'falafel', 'carrot cake']
friend_food_wrong = my_foods_wrong #Both variables point to the same list

my_foods_wrong.append('cannoli')
friend_food_wrong.append('ice cream')

print('\nWrong way - both lists are the same:')
print(my_foods_wrong)
print(friend_food_wrong)

#TRY IT YOURSELF

#4-10 Slices

superbowl_winners = ['eagles', 'chiefs', 'rams', 'bucanneers', 'patriots', 'broncos', 'seahawks', 'ravens', 'giants']

print('\nThe first three items in the list are:')
print(superbowl_winners[:3])

print('\nThe items from the middle of the list are:')
print(superbowl_winners[3:6])

print('\nThe last three items in the list are:')
print(superbowl_winners[-3:])

#4-11 My Pizzas, Your Pizzas

og_pizzas = ['grandma', 'bbq chicken', 'thin crust']

friend_pizzas = og_pizzas[:]

og_pizzas.append('buffalo chicken')

friend_pizzas.append('sausage')

print('\nMy favorite pizzas are:')
for pizza in og_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12 More Loops

print('\nThe original foods are:')
for food in my_foods[:3]:
    print(food)

print('\nThen, I added:')
for food in my_foods[-1:]:
    print(food)