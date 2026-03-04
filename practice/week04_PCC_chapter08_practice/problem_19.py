# You're building an order system for a food truck.
#
# Write a tool that accepts a size and any number of toppings,
# then prints a summary of the order

def taco_orders(number_tacos, *toppings):
    """Passes along taco order including number of tacos and toppings."""
    if number_tacos == 1:
        print(f"\nThis order is for {number_tacos} taco.")
        print(f"Here are the requested topping(s) for the taco:")
        for topping in toppings:
            print(f"\t– {topping}")
    elif number_tacos >= 1:
        print(f"\nThis order is for {number_tacos} tacos.")
        print(f"Here are the requested topping(s) for the tacos:")
        for topping in toppings:
            print(f"\t– {topping}")
    else:
        print("\nPlease select a valid number of tacos.")

taco_orders(3, 'ground beef', 'cheese', 'pico salsa')
taco_orders(1, 'carnitas', 'queso', 'salsa verde')
taco_orders(0, 'guacamole', 'beans')