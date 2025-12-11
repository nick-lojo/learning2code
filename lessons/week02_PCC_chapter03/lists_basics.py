#Lists are collections of items in a particular order
#Lists use square brackets [] with items separated by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Access elements by index (position) using square brackets
#Index 0 is the first item

print(bicycles[0])

#You can use string methods on list elements

print(bicycles[0].title())

#Index 0 = first item, index 1 = second item, index 3 = fourth item, etc

print(bicycles[1])
print(bicycles[3])

#Negative indexes count from the end
#Index -1 always gives the last item

print(bicycles[-1])

#Index -2 is second from end, -3 is third from end, etc.

print(bicycles[-2])

#You can use elements in f-strings like any other variable

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#TRY IT YOURSELF

#3-1 Names

names = ["tom", "rob", "jules", "danny"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-1].title())

#3-2 Greetings

message = f'Hello, {names[0].title()}!'
print(message)

message = f'Hello, {names[1].title()}!'
print(message)

message = f'Hello, {names[2].title()}!'
print(message)

message = f'Hello, {names[-1].title()}!'
print(message)

#3-3 Your Own List

evs = ["Tesla M3", "Tesla MY", "Tesla CT", "Tesla MS"]

message = f'I drive a {evs[0]}.'
print(message)

message = f'My next car will be a {evs[1]}.'
print(message)

message = f'The {evs[2]} is polarizing.'
print(message)

message = f'I cannot afford a {evs[-1]}.'
print(message)