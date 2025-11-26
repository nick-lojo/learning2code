result = 0
number = 1
while number <= 20:
    if number % 2 == 1:
        result = result + number
    number = number + 1
print(result)