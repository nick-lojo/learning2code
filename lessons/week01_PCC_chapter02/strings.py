#Strings can use single or double quotes
message1 = "This is a string"
message2 = 'This is a string'

#Use quotes inside strings
message3 = 'I told my friend, "Python is my favorite language!"'
message4 = "One of Python's strengths is its diverse community."

print(message1)
print(message2)
print(message3)
print(message4)

#String methods change case
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#F-strings insert variables into strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#You can use methods inside f-strings
message = f"Hello, {full_name.title()}!"
print(message)

#Adding tabs and newlines
print("Python")
print("\tPython") #Tab

print("Languages: \nPython\nC\nJavaScript") #New lines

print("Languages:\n\tPython\n\tC\n\tJavaScript") #Combined

#Stripping whitespace
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Combining change case and strip
print(favorite_language.strip().upper())

#Removing prefixes

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

#Correct - apostrophe isnide double quotes
message = "One of Python's strengths is its diverse community."
print(message)

#Try It Yourself

#2-3 Personal Message

name = "Eric"
message = f"Hello {name}, would you like to learn Python today?"
print(message)

#2-4 Name Cases

name = "drake maye"

print(name.upper())
print(name.lower())
print(name.title())

#2-5 Famous Quote

quote = '"The best revenge is massive success."'
message = f'Frank Sinatra once said, {quote}'
print(message)

#2-6 Famous Quote 2

famous_person = 'Frank Sinatra'
quote = '"The best revenge is massive success."'
message = f'{quote} - {famous_person}'
print(message)

#2-7 Stripping Names

name = '\tDrake "Drake \nMaye" Maye '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#2-8 File Extensions

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))