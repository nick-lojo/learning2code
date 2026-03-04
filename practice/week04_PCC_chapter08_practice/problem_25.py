# Problem #25
#
# You're building a flight booking tool for a travel agency.
#
# Write a tool that accepts an origin city and destination city
# and prints a booking confirmation.
# Book a flight from New York to London using the argument names explicitly.

def booking_tool(origin, destination):
    """Prints booking confirmation for a travel agency."""
    print(f"Your trip from {origin.title()} to {destination.title()} is confirmed.")

booking_tool(origin='new york', destination='london')