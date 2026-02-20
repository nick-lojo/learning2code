# You're storing information about multiple users.
#
# Create a dictionary called users.
# 
# Inside users, create two user accounts:
# - 'jdoe': a dictionary with first='John', last='Doe', role='admin'
# - 'asmith': a dictionary with first='Alice', last='Smith', role='editor'
#
# Loop through the users dictionary.
# For each user, print their username and full name (first + last).

users = {
    'jdoe':{
        'first':'John',
        'last':'Doe',
        'role':'admin'
    },
    'asmith':{
        'first':'Alice',
        'last':'Smith',
        'role':'editor'
    }
}

for username, info in users.items():
    full_name = f"{info['first']} {info['last']}"
    print(f"\nUsername: {username}")
    print(f"\tFull Name: {full_name}")