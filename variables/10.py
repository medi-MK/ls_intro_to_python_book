obj = 'ABcd' # reassignment
obj.upper() # neither, calls a method
obj = obj.lower() # reassignment
print(len(obj)) # prints the length the object, neither
obj = list(obj) # reassignment
obj.pop() # mutation
obj[2] = 'X' # mutation
obj.sort() # mutation
set(obj) # neither
obj = tuple(obj) # reassignment