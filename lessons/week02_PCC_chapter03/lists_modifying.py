#You can change any element by using its index and assignment

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#append() adds an element to the end of the list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Build lists dynamically by starting empty and appending

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#insert() adds an element at any position - specify index and value

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#del statement removes an item by index

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#pop() removes the last item but lets you use it after removing it

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#pop() can remove items from any position by specifying the index

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owed was a {first_owned.title()}.')

#remove() deletes an item by its value, not its index

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#You can also use remove() with a variable

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

#TRY IT YOURSELF

#3-4 Guest List

guest_list = []
guest_list.append('Tom Brady')
guest_list.append('Rob Gronkowski')
guest_list.append('Jon Rahm')

print(f'Dear {guest_list[0]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[-1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')

#3-5 Changing Guest List

cant_come = guest_list.pop(2)
print(cant_come)

guest_list.append('Phil Mickelson')

print(f'Dear {guest_list[0]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[-1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')

#3-6 More Guests

print(f'Dear {guest_list[0]}, {guest_list[1]}, and {guest_list[-1]}\nI am happy to inform you that we have found a bigger table, and are expecting three more guests.\nNew invitations to follow.\n- The Host')

guest_list.insert(0, 'Drake Maye')
guest_list.insert(2, 'Jimi Hendrix')
guest_list.append('Andrew Schulz')

print(f'Dear {guest_list[0]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[2]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[3]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[-2]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')
print(f'Dear {guest_list[-1]},\nWould you like to come to my dinner party?\nSincerely,\nThe Host')

#3-7 Shrinking Guest List

print(f'Dear {guest_list},\n\tI regret to inform you that the new table will not be here in time.\n\tAs such, I must shrink the guest list to two guests.\n\tYou will be informed if you can still attend shortly.\n- The Host')

removed_guest = guest_list.pop(-1)
print(f'Dear {removed_guest},\n\tI regret to inform you that you can no longer attend the dinner party.\nBest,\nThe Host')

removed_guest = guest_list.pop(1)
print(f'Dear {removed_guest},\n\tI regret to inform you that you can no longer attend the dinner party.\nBest,\nThe Host')

removed_guest = guest_list.pop(2)
print(f'Dear {removed_guest},\n\tI regret to inform you that you can no longer attend the dinner party.\nBest,\nThe Host')

removed_guest = guest_list.pop(2)
print(f'Dear {removed_guest},\n\tI regret to inform you that you can no longer attend the dinner party.\nBest,\nThe Host')

print(f'Dear {guest_list[0]},\n\tI am happy to inform you that we still have space for you at our dinner.\nSee you soon,\nThe Host')
print(f'Dear {guest_list[1]},\n\tI am happy to inform you that we still have space for you at our dinner.\nSee you soon,\nThe Host')

del guest_list[0]
del guest_list[-1]
print(guest_list)