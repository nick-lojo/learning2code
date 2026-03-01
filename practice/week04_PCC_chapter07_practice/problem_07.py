active = True
prompt = "Are you still active? (yes / no) "
message = ""

while active:
    message = input(prompt)
    if message == 'no':
        active = False
        print("Session Ended.")
    else:
        print("Session Ongoing.")