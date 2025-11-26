#Creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)

#Accessing list items by index
print(numbers[0])
print(numbers[2])
print(numbers[4])

#Negative indexes count from the end
print(numbers[-1]) #Last item
print(numbers[-2]) #Second to last

#Adding items to a list
numbers.append(60)
print(numbers)

#Append multiple items
numbers.append(70)
numbers.append(80)
print(numbers)

#Multiple append test (error expected)
#numbers.append(90, 100) (muted so code can run)

#Insert at a specific position
numbers.insert(0, 5)
print(numbers)

#Remove specific value
numbers.remove(30)
print(numbers)

#Pop removes by index and returns the value
last_item = numbers.pop() #No argument = removes last item
print("Removed:", last_item)
print("List now:", numbers)

first_item = numbers.pop(0) #Remove first item
print("Removed:", first_item)
print("List now:", numbers)

#Iteratring over a list
for num in numbers:
    print(num)

for num in numbers:
    print(num * 2)

def sum_list(lst):      #Create a function named sum_list, it accepts one parameter called lst (a list)     
    total = 0           #Create accumulator variable, starts at 0
    for number in lst:  #Loop through each item in the list, call each item "number"
        total += number #Add current number to the toal (total = total + number)
    return total        #Send the final total back to whoever called this function

result = sum_list(numbers) #Call the function, pass in your numbers list, store returned value in result
print("Sum:", result)      #Print what came back from the function

#Example: Create a function that doubles each number in a list
def double_list(lst):
    doubled = []                 #Create empty list to store results
    for number in lst:           #Loop thorugh original list
        doubled.append(number*2) #Add doubled value to new list
    return doubled               #Return the new list

result = double_list(numbers) #Call function and store result
print(result)                 #Print the returned list