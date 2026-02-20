message = ""
while message != 'quit':
    message = input("Enter a city: ")
    print(f"I'd love to go to {message.title()}!")

active = True
while active:
    message = input("Enter a city: ")
    if message == 'quit':
        active = False
    print(f"I'd love to go to {message.title()}!")