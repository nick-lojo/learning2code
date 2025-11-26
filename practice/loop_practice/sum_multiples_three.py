result = 0
number = 0
while number <= 30:
    if number % 3 == 0:
        result = result + number
    number = number + 1
print(result)