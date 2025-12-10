#Attempt 1 (using lists_intro.py)

list = [10, 20, 30, 40]

def count_items(list):
    total = 0
    for number in list:
        total += number
    return total

result = count_items(list)
print(result)