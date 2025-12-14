#Tuples - immutable lists (cannot be changed after creation)
#Use parentthases () instead of brackets []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#This will produce an error:
#dimensions[0] = 250

#Looping through a tuple works like a list

for dimension in dimensions:
    print(dimension)

#You can't modify a tuple, but you can reassign the variable to a new tuple

print('\nOriginal dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #Assign a completely new tuple

print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

#TRY IT YOURSELF

#4-13 Buffet

buffet_foods = ('sesame chicken', 'lo mein', 'fried rice', 'orange chicken', 'dumplings')

print('\nThe buffet offers:')
for food in buffet_foods:
    print(food)

#buffet_foods[3] = 'scallion pancake'

buffet_foods = ('sesame chicken', 'wonton soup', 'fried rice', 'scallion pancakes', 'dumplings')

print('\nThe new menu offers:')
for food in buffet_foods:
    print(food)