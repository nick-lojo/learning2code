# You're writing a script for a data migration tool.
#
# Review this code and explain why it will never stop running.
# Fix it so the loop terminates correctly.

# server = 1
# while server <= 3:
#     print(f"Migrating server {server}...")

# This will run forever because we are not changing the value of server.
# Server always equals 1. 1 is <= 3. Since it never changes, it will print 1
# forever.

# Correct Solution:

server = 1
while server <= 3:
    print(f"Migrating server {server}...")
    server = server + 1