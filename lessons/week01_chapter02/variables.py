#This program demonstrates basic variable usage

message = "Hello Python world!"
print(message)

#Variables can be reassigned to new values

message = "Hello Python Crash Course world!"
print(message)

#Variable naming rules – valid examples
student_name = "Ada"
age_1 = 25
_private_value = 100

print(student_name)
print(age_1)
print(_private_value)

#This will cause a NameError - mispelled variable

test_message = "This should work"
#print(test_mesage) mispelled on purpose

#Fixed - correct spelling
test_message = "This should work"
print(test_message) #Now spelled correctly