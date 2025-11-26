def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")

#Test to understand the difference between , and +

name = "Alice"
print("Hello," + name + "!")
print("Hello,", name, "!")

#Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

total = add_numbers(10, 7)
doubled = total * 2
print(doubled)

#Function that prints (cant't use results)
def add_and_print(a, b):
    print(a + b)

#Function that returns (can use result)
def add_and_return(a, b):
    return a + b

x = add_and_print(5, 3) #prints 8, but x gets None
y = add_and_return(5, 3) #returns 8, y gets 8

print("x is:", x)
print("y is:", y)

#Example
def calculate_print(x):
    print(x + 10) #Announces the answer

def calculate_return(x):
    return x + 10 #Hands you the answer

#With print:
result1 = calculate_print(5) #Prints "15" but result 1 gets nothing

#With return:
result2 = calculate_return(5) #Returns 15, result2 now holds 15
print(result2) #Prints "15" becauyse you have the actual value
print(result2 * 2) #Prints "30" because you can use it!