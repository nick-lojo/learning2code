#sort() changes the list order permanently to alphabetical

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sort() can reverse the alphabetical order with reverse = True

cars.sort(reverse = True)
print(cars)

#sorted() displays the list in order but doesn't change the original

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

#reverse() flips the list order permanently (not alphabetically, just backwards)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#You can reverse it again to get back to the original order

cars.reverse()
print(cars)

#len() returns the number of items in a list

print(len(cars))

#TRY IT YOURSELF

#3-8 Seeing the World

vacation = []
vacation.append('Hokkaido')
vacation.append('Amsterdam')
vacation.append('Chongqing')
vacation.append('Honolulu')
vacation.append('Melbourne')
print(vacation)

print(sorted(vacation))

print(vacation)

print(sorted(vacation, reverse = True))

print(vacation)

vacation.reverse()
print(vacation)

vacation.reverse()
print(vacation)

vacation.sort()
print(vacation)

vacation.sort(reverse = True)
print(vacation)

#3-9 Dinner Guests

guest_list = []
guest_list.append('Drake Maye')
guest_list.append('Tim Dillon')
guest_list.append('Jimi Hendrix')

print(f'Dear guests,\n\tThere will be {len(guest_list)} at dinner this evening.\nBest,\nHost')

#3-10 Every Function

every_function = []

every_function.append('Nozawa Onsen')
every_function.append('Mississippi River')
print(every_function)

every_function.insert(1, 'Mandarin')
print(every_function)

del every_function[-1]
print(every_function)

language = every_function.pop(-1)
print(language)

every_function.append(language)
print(every_function)

every_function.remove('Mandarin')
print(every_function)

every_function.append('Sumida')
every_function.append('Japan')
every_function.append('Japanese')
every_function.insert(3, 'Tokyo')
print(every_function)

every_function.sort()
print(every_function)

print(sorted(every_function))

every_function.reverse()
print(every_function)

every_function.reverse()
print(every_function)

print(len(every_function))