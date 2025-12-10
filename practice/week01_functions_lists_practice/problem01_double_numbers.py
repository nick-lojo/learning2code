#Practice referencing notes

#Attempt 1

numbers = [1, 2, 3]
def double_numbers(numbers):
    print(numbers * 2)
double_numbers(numbers)

#Attempt 2; Found exact code in lists_intro.py
lst = [1, 2, 3]

def double_numbers(lst):
    doubled = []
    for number in lst:
        doubled.append(number*2)
    return(doubled)
result = double_numbers(lst)
print(result)