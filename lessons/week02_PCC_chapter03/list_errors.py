#Asking for an index that doesn't exist causes an IndexError

motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3]) #This would cause an error - only indexes 0, 1, 2 exist

#The safe way to access the last item is with index -1
print(motorcycles[-1])

#Index - 1 only fails on empty lists

motorcycles = []
#print(motorcycles[-1]) #This would cause an error - no items exist

#If you get index errors, print the list or its length to debug

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(len(motorcycles))