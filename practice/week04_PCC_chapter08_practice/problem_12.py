# You're building an order tool for a sandwich shop.
#
# Write a tool that accepts any number of toppings for a sandwich
# and prints a summary of the order.
# Place three orders with different numbers of toppings.

def sandwich_order(*toppings):
    """Allows customer to add an unlimited number of toppings to their
    sandwich."""
    for topping in toppings:
        print(f"Adding {topping} to your sandwich.")
    print("Your sandwich is ready.\n")

sandwich_order('chicken cutlet')
sandwich_order('ham', 'cheese')
sandwich_order('bacon', 'lettuce', 'tomato')