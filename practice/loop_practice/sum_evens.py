result = 0
number = 1
while number <= 10:
    if number % 2 == 0:
        result = result + number
    number = number + 1
    print(result)