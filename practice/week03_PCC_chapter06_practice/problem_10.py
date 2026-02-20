# You're checking user permissions.
#
# You have a user dictionary:
# - username: 'alice'
# - role: 'editor'
#
# Check if the user has an 'admin_level' key.
# If it exists, print the value.
# If it doesn't exist, print 'No admin level assigned'.

user = {
    'username':'alice',
    'role':'editor'
}

admin_level = user.get('role', 'No admin level assigned')
print(admin_level)