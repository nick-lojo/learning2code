total = 0
number = 1
while number <= 20:
    if number % 2 == 0:
        total = total + number
    else:
        print(number)
    number = number + 1
print("Total Sum of Evens:",total)