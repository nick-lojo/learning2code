# You're managing a restaurant menu system.
#
# Create a dictionary called menu with three items:
# - 'burger': price=12, category='entree',
# ingredients=['beef', 'lettuce', 'tomato']
#
# - 'salad': price=8, category='appetizer',
# ingredients=['lettuce', 'cucumber', 'dressing']
#
# - 'fries': price=5, category='side'
#
# Note: 'fries' has no ingredients list.
#
# For each menu item:
# - Print the item name and price
# - Try to print the ingredients. If no ingredients are listed, print
# 'Ingredients not available'

menu = {
    'burger':{
        'price':12,
        'category':'entree',
        'ingredients':['beef', 'lettuce', 'tomato']
    },
    'salad':{
    'price':8,
    'category':'appetizer',
    'ingredients':['lettuce', 'cucumber', 'dressing']
    },
    'fries':{
        'price':5,
        'category':'side'
    }
}

for item, details in menu.items():
    print(f"\nItem: {item.title()}")
    print(f"\tPrice: ${details['price']}")
    ingredients = details.get('ingredients', 'Ingredients not available')
    print(f"\tIngredients: {ingredients}")