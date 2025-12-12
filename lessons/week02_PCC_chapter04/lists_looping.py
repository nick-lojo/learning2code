#For loops - running the same action on every item in a list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#How for loops work:
# 1. Python pulls the first item from the list (magicians)
# 2. Assigns it to the temporary variable (magician)
# 3. Executes the indented code block
# 4. Returns to step 1 with the next item
# 5. Repeats until no items remain

#Naming convention: for singular in plurals
#Examples: for cat in cats, for dog in dogs, for item in items

#Adding more work inside the loop

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')

#Multiple lines inside a loop - all indented lines execute for each item

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Code after the loop - not indented, runs once after loop finishes

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone, that was a great magic show!")

#Common indentation errors to avoid:

#Error 1: Forgetting to indent

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician) #This would cause IndentationError

#Error 2: Forgetting to indent additional lines

#for magician in magicians:
#   print(f'{magician.title()}, that was a great trick!')
#print(f"I can't wait to see your next trick, {magcian.title()}.\n") #Only runs once at end

#Error 3: Indenting unnecessarily after the loop

#for magician in magicians:
#   print(f'{magician.title()}, that was a great trick!')
#   print("Thank you!") #This would repeat for each magician instead of once

#Error 4: Forgetting the colon

#for magician in magicians
#   print(magician) #SyntaxError: expected ':'

#TRY IT YOURSELF

#4-1 Pizzas

pizzas = ['grandma', 'bbq chicken', 'thin crust']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f'I like {pizza} pizza.\n')
print('I really love pizza!')

#4-2 Animals

animals = ['grizzly bear', 'polar bear', 'panda']
for animal in animals:
    print(animal)

for animal in animals:
    print(f'A {animal.title()} is a type of bear.\n')

print('Never pet a bear in the wild!')