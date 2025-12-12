#range() generates a series of numbers
#range(start, stop) - stops BEFORE the stop number (off-by-one behavior)

for value in range(1, 5):
    print(value)

#To print 1 to 5, use range(1, 6)

for value in range(1, 6):
    print(value)

#range() with one argument starts at 0

for value in range(6):
    print(value)

#Convert range() to a list using list()

numbers = list(range(1,6))
print(numbers)

#range with a third argument - the step size (skip numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Building a list of square numbers using a loop

squares = []               #Create an empty list to store results
for value in range(1, 11): #Loop through numbers 1 to 10
    square = value ** 2.   #Calculate the square (value times itself)
    squares.append(square) #Add the squared result to the list

print(squares) #Display the final list

#Same result, more concise - skip the temporary variable

squares_v2 = []
for value in range(1, 11):
    squares_v2.append(value ** 2) #Calculate and append in one line

print(squares_v2)

#Built-in functions for numerical lists

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] #or digits = list(range(10))
print(f'Min: {min(digits)}')
print(f'Max: {max(digits)}')
print(f'Sum: {sum(digits)}')

#List comprehension - creates a list in one line
#Format: [expression for item in iterable]

squares_comp = [value ** 2 for value in range(1,11)]
print(squares_comp)

#List comprehension anatomy:
#[value ** 2    for value in range(1, 11)]
# ^ expression  ^ for loop to generate values
#Result gets automatically appended to the new list

#TRY IT YOURSELF

#4-3 Counting to Twenty

for value in range(1, 21):
    print(value)

#4-4 One Million

one_million = list(range(1, 1000001))
for value in one_million:
    print(value)

#4-5 Summing a Million

sum_million = list(range(1, 1000001))
print(f'Min: {min(sum_million)}')
print(f'Max: {max(sum_million)}')
print(f'Sum: {sum(sum_million)}')

#4-6 Odd Numbers

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

#4-7 Threes

threes = list(range(3, 31, 3))
for number in threes:
    print(number)

#4-8 Cubes

cubes = []
for value in range(1, 11):
    print(value ** 3)

#4-9 Cube Comprehension

cubes_comp = [value ** 3 for value in range(1, 11)]
print(cubes_comp)