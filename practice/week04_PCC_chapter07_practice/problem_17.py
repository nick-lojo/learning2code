responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    shirt_size = input("What is your t-shirt size? ")

    responses[name] = shirt_size

    keep_polling = input("Are there any more participants to register? (yes / no) ")
    if keep_polling == 'no':
        polling_active = False

print("\n–––Results–––")
for name, shirt_size in responses.items():
    print(f"\t{name.title()} needs a size {shirt_size.upper()} shirt.")