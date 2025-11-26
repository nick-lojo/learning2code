count = 0
number = 1
while number <= 100:
    if number % 8 == 0:
        count = count + 1
    number = number + 1
print(count)