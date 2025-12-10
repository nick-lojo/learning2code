#Attempt 1: (Referenced functions_intro.py)

#def add_exclamation(word):
#    print(word + "!")

#add_exclamation("Hello")
#add_exclamation("world")

#Attempt 2: (Referenced problem01)

lst = ["hello", "world"]

def add_exclamation(lst):
    exclamation_added = []
    for word in lst:
        exclamation_added.append(word+"!")
    return(exclamation_added)
result = add_exclamation(lst)
print(result)