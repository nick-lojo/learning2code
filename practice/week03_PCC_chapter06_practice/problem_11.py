# You're displaying server information.
#
# You have a server dictionary:
# - hostname: 'web-server-01'
# - ip_address: '192.168.1.100'
# - status: 'active'
# - port: 8080
#
# Print each piece of information in this format:
# Hostname: web-server-01
# Ip_address: 192.168.1.100
# Status: active
# Port: 8080
#
# Use a loop to print all key-value pairs.

server = {
    'hostname':'web-server-01',
    'ip_address':'192.168.1.100',
    'status':'active',
    'port':8080
}

for key, value in server.items():
    print(f'{key.title()}: {value}')