# You're building an event registration tool for a conference platform.
#
# Write a tool that accepts an attendee's first and last name plus
# any number of sessions they want to attend.
# Register one attendee for a single session and one for three sessions.

def event_registration(first_name, last_name, *sessions):
    """Enables attendees to register for sessions at an event."""
    full_name = f"{first_name} {last_name}"
    print(f"\nName: {full_name.title()}")
    print(f"Session Registration:")
    for session in sessions:
        print(f"\t{session.title()}")

event_registration('jane', 'doe', 'analyzing risk')
event_registration('john', 'smith', 'how to implement enterprise risk management',
                   'assessing black swans', 'building resiilient systems')