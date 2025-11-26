number = 5
result = 0
while number <= 25:
    if number % 5 == 0:
        result = number + result
    number = number + 1
print(result)